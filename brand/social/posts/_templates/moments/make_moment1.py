#!/usr/bin/env python3
"""Moment 1 (tickets on sale) text-led graphic, no screenshot and no countdown.
Usage: python3 make_moment1.py "Tampa" "22-25 Oct"   -> moment1-tampa.svg / .png in this folder
"""
import re, subprocess, sys
city, dates = sys.argv[1], sys.argv[2]
src = open('../../events/birmingham/slide1-hook.svg').read()
logo = re.search(r'(<g transform="translate\(80,64\).*?</g>\s*<text x="142".*?</text>)', src, re.S).group(1)
font = 'font-family="Arial, sans-serif"'
svg = f'''<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
  <rect width="1080" height="1080" fill="#374D59"/>
  {logo}
  <text x="80" y="330" {font} font-size="24" font-weight="700" letter-spacing="4" fill="#E22424">HYROX · {city.upper()}</text>
  <text x="78" y="400" {font} font-size="60" font-weight="700" fill="#ffffff">Got your ticket?</text>
  <text x="78" y="470" {font} font-size="60" font-weight="700" fill="#ffffff">Need a partner?</text>
  <text x="78" y="590" {font} font-size="24" font-weight="400" fill="rgba(255,255,255,0.78)">HYROX {city}, {dates}. HyPair matches you</text>
  <text x="78" y="624" {font} font-size="24" font-weight="400" fill="rgba(255,255,255,0.78)">with a doubles partner by pace and goal,</text>
  <text x="78" y="658" {font} font-size="24" font-weight="400" fill="rgba(255,255,255,0.78)">not just whoever asks first.</text>
  <text x="78" y="900" {font} font-size="26" font-weight="700" letter-spacing="1" fill="#F2D079">hypair.app</text>
</svg>'''
name = f'moment1-{city.lower().replace(" ", "-")}'
open(f'{name}.svg', 'w').write(svg)
subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1080', '-o', f'{name}.png', f'{name}.svg'], check=True)
print('wrote', name)
