#!/usr/bin/env python3
"""Where would you race next? map (1080x1080). Highlights countries where HyPair lists events (Canada deliberately left out: marketing paused)."""
import json, subprocess
W, H = 1080, 1080
LON0, LON1, LAT0, LAT1 = -132, 180, -52, 64
MX, MY, MW = 30, 470, 1020            # map box
sx = MW / (LON1 - LON0)
MH = (LAT1 - LAT0) * sx
def pt(lon, lat):
    if lon < -132: lon += 360   # wrap Alaska/Aleutians off the left edge instead of far right
    return MX + (lon - LON0) * sx, MY + (LAT1 - lat) * sx
ON = {'United States of America', 'Ireland', 'United Kingdom', 'Australia', 'South Africa', 'New Zealand'}
cities = {
 'United States of America': [(33.84,-117.91),(33.75,-84.39),(41.88,-87.63),(32.78,-96.8),(39.74,-104.99),(29.76,-95.37),(36.17,-115.14),(25.79,-80.13),(36.16,-86.78),(33.45,-112.07),(45.52,-122.68),(32.72,-117.16),(27.95,-82.46)],
 'Ireland': [(53.35,-6.26)],
 'United Kingdom': [(52.49,-1.89),(51.48,-3.18),(55.86,-4.25),(51.51,-0.13),(53.48,-2.24)],
 'Australia': [(-27.47,153.03),(-37.81,144.96)],
 'South Africa': [(-33.92,18.42),(-26.2,28.05)],
 'New Zealand': [(-36.85,174.76)],
}
n_cities = sum(len(v) for v in cities.values())
geo = json.load(open('world.geo.json'))
def rings(geom):
    if geom['type'] == 'Polygon': return [geom['coordinates']]
    return geom['coordinates']
paths = []
for f in geo['features']:
    name = f['properties']['name']
    if name == 'Antarctica': continue
    on = name in ON
    d = ''
    for poly in rings(f['geometry']):
        for ring in poly:
            xs = [p[0] for p in ring]
            if max(xs) - min(xs) > 180:
                ring = [(x + 360 if x < 0 else x, y) for x, y in ring]   # crosses the dateline: unwrap, the clipPath trims the overflow
            xs = [p[0] for p in ring]
            if max(xs) < LON0: continue
            pts = [((MX + (x - LON0) * sx), MY + (LAT1 - y) * sx) for x, y in ring]
            d += 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + 'Z'
    if not d: continue
    fill = '#2A3340' if not on else '#3A3322'
    stroke = '#46505E' if not on else '#F2D079'
    sw = 0.6 if not on else 1.1
    paths.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')
dots = []
for c, lst in cities.items():
    for lat, lon in lst:
        x, y = pt(lon, lat)
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#F2D079" opacity="0.28"/><circle cx="{x:.1f}" cy="{y:.1f}" r="5.2" fill="#F2D079"/>')
logo = '<g transform="translate(80,64) scale(0.187)"><path d="M350,399.3c-26.8,0-48.6,21.8-48.6,48.6c0,26.8,21.8,48.6,48.6,48.6s48.6-21.8,48.6-48.6C398.6,421.1,376.8,399.3,350,399.3z M350,463.9c-8.8,0-16-7.2-16-16c0-8.8,7.2-16,16-16c8.8,0,16,7.2,16,16C366,456.7,358.8,463.9,350,463.9z" fill="#F2D079" transform="translate(-226,-154.1)"/><polygon points="412.1,154.1 374.4,154.1 374.4,281.6 325.6,281.6 325.6,154.1 287.9,154.1 287.9,319.2 412.1,319.2" fill="#F2D079" transform="translate(-226,-154.1)"/><polygon points="401.5,336.6 298.5,336.6 298.4,336.8 226,409.1 226,496.4 258.5,496.4 258.5,422.6 306.9,374.3 393.1,374.3 441.5,422.6 441.5,496.4 474,496.4 474,409.1" fill="#F2D079" transform="translate(-226,-154.1)"/></g>'
F = 'font-family="Arial, Helvetica, sans-serif"'
svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" fill="#0F1318"/>
{logo}
<text x="80" y="215" {F} font-size="26" font-weight="700" letter-spacing="6" fill="#F2D079">FIND A HYROX PARTNER</text>
<text x="80" y="310" {F} font-size="88" font-weight="800" fill="#ffffff">Where would</text>
<text x="80" y="400" {F} font-size="88" font-weight="800" fill="#ffffff">you race next?</text>
<defs><clipPath id="mapclip"><rect x="{MX}" y="{MY-10}" width="{MW}" height="{MH+20:.0f}"/></clipPath></defs>
<g clip-path="url(#mapclip)">{''.join(paths)}{''.join(dots)}</g>
<text x="80" y="{MY+MH+80:.0f}" {F} font-size="34" font-weight="700" fill="#ffffff">6 countries, {n_cities} cities, and growing.</text>
<text x="80" y="{MY+MH+124:.0f}" {F} font-size="28" fill="rgba(255,255,255,0.78)">Tell us where we should go next.</text>
</svg>'''
open('where-next.svg', 'w').write(svg)
subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1080', '-o', 'where-next.png', 'where-next.svg'], check=True)
print('ok', n_cities, 'cities; map height', round(MH))
