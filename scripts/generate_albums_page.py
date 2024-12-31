import os
import urllib.parse

image_folder = "pages/album-images"
output_file = "pages/albums.html"
youtube_music_search_url = "https://music.youtube.com/search?q="

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>albums</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">
</head>
<body>
    <div class="container">
        <header>
            <h1>альбоми</h1>
        </header>
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="https://nstr1.github.io/nstr.github.io">home</a></li>
                <li class="breadcrumb-item active" aria-current="page">альбоми</li>
            </ol>
        </nav>
        <main class="gallery">
"""

for image_file in sorted(os.listdir(image_folder)):
    if image_file.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        album_info = os.path.splitext(image_file)[0].replace("-", " ").replace("_", " ").split(" ")
        album_title = " ".join(album_info[:-1]).lower()
        artist_name = album_info[-1].lower()

        query = f"{album_title} {artist_name}"
        link_url = youtube_music_search_url + urllib.parse.quote(query)

        html_content += f"""
            <div class="gallery-item">
                <img src="album-images/{image_file}" class="album-art">
                <a href="{link_url}" target="_blank">{album_title} {artist_name}</a>
            </div>
        """

html_content += """
        </main>
    </div>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)

