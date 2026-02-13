#!/usr/bin/env python3
"""
Generate Open Graph social sharing image for Valentine's Day project
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_og_image():
    # Create image with Open Graph recommended dimensions (1200x630)
    width, height = 1200, 630
    image = Image.new('RGB', (width, height), color='#ff9a9e')
    
    # Create gradient background
    draw = ImageDraw.Draw(image)
    for y in range(height):
        # Create gradient from top to bottom
        r = int(255 - (255 - 254) * y / height)
        g = int(154 - (154 - 207) * y / height) 
        b = int(158 - (158 - 247) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Add semi-transparent overlay card
    card_width, card_height = 800, 400
    card_x = (width - card_width) // 2
    card_y = (height - card_height) // 2
    
    # Draw card with rounded corners effect
    card_color = (255, 255, 255, 230)
    card_image = Image.new('RGBA', (card_width, card_height), card_color)
    image.paste(card_image, (card_x, card_y), card_image)
    
    # Try to load fonts, fallback to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        subtitle_font = ImageFont.truetype("arial.ttf", 30)
        emoji_font = ImageFont.truetype("seguiemj.ttf", 80)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        emoji_font = ImageFont.load_default()
    
    # Draw text
    draw = ImageDraw.Draw(image)
    
    # Title
    title_text = "Will You Be My Valentine?"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = card_y + 80
    draw.text((title_x, title_y), title_text, fill='#2b0b18', font=title_font)
    
    # Emoji
    emoji_text = "💘"
    emoji_bbox = draw.textbbox((0, 0), emoji_text, font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_x = (width - emoji_width) // 2
    emoji_y = title_y + 80
    draw.text((emoji_x, emoji_y), emoji_text, font=emoji_font)
    
    # Subtitle
    subtitle_text = "Can you catch the runaway No button?"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = emoji_y + 100
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill='#7a3b4f', font=subtitle_font)
    
    # Add some decorative hearts
    heart_positions = [
        (100, 100), (1100, 100), (100, 530), (1100, 530),
        (200, 50), (1000, 50), (200, 580), (1000, 580)
    ]
    
    for pos in heart_positions:
        draw.text(pos, "❤", fill='rgba(255, 255, 255, 180)', font=emoji_font)
    
    # Save image
    image.save('og-image.png', 'PNG')
    print("Open Graph image created successfully: og-image.png")

if __name__ == "__main__":
    create_og_image()
