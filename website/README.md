# StrictDoc website (Hugo)

Dev notes for this Hugo site. Do not put notes/README files under `layouts/` —
Hugo compiles every file in that tree as a Go template regardless of
extension, and literal shortcode syntax like `{{< video ... >}}` in a
plain-text example will fail the build.

## Shortcodes

### video

Embeds a looping, muted, autoplaying video (webm + mp4 fallback) into a
content page.

Usage in any `content/*.md`:

```
{{</* video src="hello_world" */>}}
```

`src` is the file name without extension. It expects both files to exist:

```
website/static/video/hello_world.webm
website/static/video/hello_world.mp4
```

Template: `layouts/shortcodes/video.html`.
Styling: `.content-video` in `static/css/main.css`.
