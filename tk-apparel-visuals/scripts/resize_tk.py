#!/usr/bin/env python3
"""Convert an already-isolated/white-background product image to a square TK canvas.
This tool does not remove a photographic background; isolate that first.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

def convert(source: Path, target: Path, size: int = 2000):
    with Image.open(source) as original:
        im=ImageOps.exif_transpose(original).convert("RGBA")
        im.thumbnail((size,size), Image.Resampling.LANCZOS)
        canvas=Image.new("RGBA",(size,size),(255,255,255,255))
        canvas.alpha_composite(im,((size-im.width)//2,(size-im.height)//2))
        target.parent.mkdir(parents=True,exist_ok=True)
        canvas.convert("RGB").save(target,"PNG" if target.suffix.lower()==".png" else "JPEG", quality=94)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("source",type=Path)
    parser.add_argument("target",type=Path)
    parser.add_argument("--size",type=int,default=2000)
    args=parser.parse_args()
    convert(args.source,args.target,args.size)
