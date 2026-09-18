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

Publish by material content, not by application build number. Reuse unchanged
licenses, decoder sources, frameworks and instructions at their existing URLs.
Only update the fixed license catalogs when their content changes. Historical
notice directories remain available for compatibility and are no longer copied
for each TestFlight build.

When application object files or resources actually change, publish the necessary
matching relinking attachment through Releases. Compare content hashes first and
reuse an identical existing artifact. Binary archives never belong in Git.
The stable downloads page links to Releases; per-build verification records are
kept in the private application repository. Public titles use
`RemoteFS iOS 1.2.1 · Build 17`; filenames and tags use ASCII hyphens.
Never upload application source, signing credentials, review credentials or
customer data. Do not replace an existing attachment with different contents.
