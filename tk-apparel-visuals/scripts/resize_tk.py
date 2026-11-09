#!/usr/bin/env python3
"""Fit an already-isolated/white-background product image onto a TK 3:4 white canvas (default 1800x2400).
This tool does not remove a photographic background; isolate that first.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

def convert(source: Path, target: Path, width: int = 1800, height: int = 2400):
    with Image.open(source) as original:
        im=ImageOps.exif_transpose(original).convert("RGBA")
        im.thumbnail((width,height), Image.Resampling.LANCZOS)
        canvas=Image.new("RGBA",(width,height),(255,255,255,255))
        canvas.alpha_composite(im,((width-im.width)//2,(height-im.height)//2))
        target.parent.mkdir(parents=True,exist_ok=True)
        canvas.convert("RGB").save(target,"PNG" if target.suffix.lower()==".png" else "JPEG", quality=94)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("source",type=Path)
    parser.add_argument("target",type=Path)
    parser.add_argument("--width",type=int,default=1800)
    parser.add_argument("--height",type=int,default=2400)
    args=parser.parse_args()
    convert(args.source,args.target,args.width,args.height)
