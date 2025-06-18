import waveassist

waveassist.init()

# Fetch the comic data from the previous node
comic_data = waveassist.fetch_data("comic_data")

# Extract image URL, title, and alt text
img_url = comic_data["img"]
title = comic_data["title"]
alt_text = comic_data["alt"]

# Create email content with embedded image
subject = f"Daily xkcd: {title}"
html_content = f"""
<h2>{title}</h2>
<img src="{img_url}" alt="{alt_text}" style="max-width:100%; height:auto;" />
<p>{alt_text}</p>
<p>Source: <a href="https://xkcd.com/">xkcd.com</a></p>
"""

# Send email without attachment
waveassist.send_email(subject, html_content=html_content)

# Store completion status
waveassist.store_data("email_sent", True)
