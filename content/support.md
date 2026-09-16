# RemoteFS Support

RemoteFS helps users browse and manage remote files over SFTP, FTP, and WebDAV.

## Before Contacting Support

Please include the following information when reporting an issue:

- RemoteFS version.
- macOS, iOS, or iPadOS version and device model.
- Protocol in use: SFTP, FTP, or WebDAV.
- A short description of the server type, for example OpenSSH SFTP, Apache WebDAV, or NAS WebDAV.
- The operation that failed, such as connect, list directory, preview, upload, download, rename, or delete.
- The exact error message shown by the app.

Do not send passwords, private keys, passphrases, sensitive server names, sensitive file paths, or sensitive file contents.

## Common Troubleshooting

### Connection Fails

Verify the server address, port, username, password, and protocol. For SFTP, confirm that the server accepts the selected authentication method. For WebDAV, confirm that the URL points to the correct WebDAV root.

### Transport Security

Use SFTP or WebDAV over HTTPS for sensitive data. Plain FTP is not encrypted by RemoteFS and should only be used on networks where that risk is acceptable.

### Preview Is Slow

Preview speed depends on the remote server, network latency, and file size. RemoteFS caches thumbnails locally. You can adjust or clear the thumbnail cache in Settings.

### Local Discovery Finds Nothing

Choose Scan Local Network from Storage and allow local-network access when prompted. Discovery uses Bonjour advertisements and cannot find every device on every network. Check that the server advertises a supported service, or add its address manually. Guest Wi-Fi isolation, VLAN boundaries, and VPN routing may prevent discovery.

### A Video Does Not Play

In native Apple builds, native playback is supplemented by an embedded compatibility player for additional AVI, MKV, and WebM codec combinations. A filename extension alone does not identify its codec or guarantee support. Report the container, codec/profile when known, app version, and sanitized error; do not send private video content. Network errors during a read are distinct from unsupported decoding. DRM-protected media is not supported.

### Upload or Download Fails

Check that the destination folder is writable and that the remote server has enough available space. If the network is unstable, retry after reconnecting.

### Cached Thumbnails Look Stale

RemoteFS keys thumbnail cache entries by path, size, and modification time when available. If the server reports unstable modification times, clear the thumbnail cache from Settings.

## Data and Privacy

RemoteFS does not collect analytics or send remote file data to developer-operated servers. See [Privacy Policy](privacy-policy.md) for details.

## Third-Party Notices

RemoteFS includes third-party open source components. Native Apple builds provide full local notice documents in Settings under Open Source Licenses, backed by the bundled `NativeNotices` resources. Older Mac builds may contain third-party notices as `ThirdPartyNotices.md`.

## Support Contact

Open a support issue at [github.com/Moonight-Studio/RemoteFS/issues](https://github.com/Moonight-Studio/RemoteFS/issues). When reporting an issue, include the troubleshooting details listed above and remove any private server names, credentials, or sensitive file paths.

## Trial and Connection Removal

Version 1.2.0 test builds offer a seven-day trial and a one-time lifetime unlock, without automatic billing or a subscription. Use Restore Purchases to restore verified Apple purchases. TestFlight purchases are free test transactions and do not transfer to the production app.

In iOS 1.2.0 (14), disconnecting retains offline media indexes. Storage → ⋯ → Remove Connection removes saved configuration, credentials and that connection’s media index; it does not delete server files or securely erase every preview cache. Use Settings for cache management.
