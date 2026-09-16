# RemoteFS · Moonight Studio

Public support, privacy policy, third-party notices and versioned source/relinking materials.

- [Website](https://moonight-studio.github.io/RemoteFS/)
- [Support](https://moonight-studio.github.io/RemoteFS/support.html) · [中文支持](https://moonight-studio.github.io/RemoteFS/support-zh.html)
- [Privacy](https://moonight-studio.github.io/RemoteFS/privacy-policy.html)
- [Licenses](https://moonight-studio.github.io/RemoteFS/legal.html)
- [Downloads](https://moonight-studio.github.io/RemoteFS/downloads.html)

The proprietary RemoteFS application source is not included. Third-party materials retain their own licenses; the library modification and relinking permissions are described on the licenses page and in each archive.

This is a new public support repository. It contains materials for the latest selected builds; earlier releases are not copied here. Existing application versions may still reference the previous support and materials locations.

## Maintaining the site

Edit `content/*.md`, run `python3 build.py`, and commit the generated HTML with the source. GitHub Pages deploys the root of `main`. No external scripts, fonts, analytics, or package installation are required.

For each app release, publish the exact verified relinking kit as a Release asset; update `downloads.json` and `content/downloads.md` with its platform, version, build and hash. Never upload app source, signing credentials, review credentials, or customer data. Do not replace historical archives with materials for a different build.
