# RemoteFS Privacy Policy

Last updated: 2026-09-16

RemoteFS is a remote file system browser for desktop and mobile devices for SFTP, FTP, and WebDAV servers. The app is designed to operate locally on the user's device.

## Data Collection

The RemoteFS app does not collect, sell, or share personal data with the developer. Information you voluntarily submit in a support request is handled separately, as described below.

The app does not include analytics, advertising SDKs, tracking SDKs, or crash-reporting services. RemoteFS does not send usage events, file names, server addresses, credentials, or browsing history to the developer.

## Data Stored Locally

RemoteFS stores the following data locally on the user's device:

- Saved connection metadata, such as protocol, server address, port, username, remote path, and display preferences.
- Credentials, such as passwords, in the operating system credential store. On macOS this is Keychain. In builds where SFTP private-key authentication is available, private-key passphrases are also stored in the operating system credential store; the Mac App Store candidate disables SFTP private-key file authentication and does not persist local private-key paths.
- Recent files and folders, bookmarks, UI preferences, keyboard shortcuts, and theme preferences.
- Thumbnail cache files generated from remote media, subject to the cache size limit configured in Settings.

Preview and playback may create private local cache files. These are separate from user-requested downloads and can be removed through cache management in Settings. Trial expiration does not erase connections or caches, and cache controls remain available.

## Trial and Purchases

Apple builds use StoreKit for a seven-day free trial and a one-time lifetime unlock. Apple processes payments and keeps purchase history under its own privacy policy. RemoteFS verifies signed purchase records on the device to restore purchases and determine access. RemoteFS does not receive payment-card details and does not send purchase records to a developer-operated server. A local Keychain timestamp helps prevent restarting or extending an active trial by changing the device clock. No analytics or subscription SDK is added.

Apple 版本通过 StoreKit 提供七天免费试用和一次付费永久解锁。Apple 处理付款，购买凭证在设备上验证；RemoteFS 不收集银行卡信息，也不向开发者服务器发送购买记录。钥匙串中的本地时间记录用于保护试用连续性。试用到期后仍可使用设置与缓存管理。

## Network Access

RemoteFS connects to servers configured or selected by the user and to Apple services for purchases and restoration. Remote file traffic may include:

- Directory listings and metadata requests.
- File reads for preview, thumbnail generation, streaming, and download.
- File writes for upload, rename, delete, and folder creation.

RemoteFS does not proxy remote file traffic through developer-operated servers.

Transport security depends on the protocol and server selected by the user. SFTP uses SSH, and WebDAV can use HTTPS/TLS when the user enters an HTTPS URL. Plain FTP is not encrypted by RemoteFS; users should choose SFTP or HTTPS WebDAV for sensitive data.

## Credentials

Credentials are stored in the system credential store and are not written to app configuration files in plain text. Users can remove saved credentials by deleting the related saved connection or by clearing credentials from the operating system credential manager.

## Cache Management

Thumbnail cache is stored in the app cache directory. Users can configure the thumbnail cache size limit and clear the cache from Settings. Cache entries are removed automatically when the configured size limit is exceeded.

## Logs

RemoteFS should not log passwords, private keys, passphrases, or full credential-bearing URLs. If diagnostic logs are added in future versions, they must avoid secrets and private file contents.

## Contact

For privacy questions or support requests, open an issue at [github.com/Moonight-Studio/RemoteFS/issues](https://github.com/Moonight-Studio/RemoteFS/issues). Do not include credentials, private keys, passphrases, sensitive file paths, or sensitive file contents in public reports.

## Website and Support Requests

This support website is hosted by GitHub Pages. GitHub logs visitors’ IP addresses for security purposes under [GitHub’s privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). This website adds no analytics, advertising, cookies, or third-party scripts.

GitHub issues are public. Information you voluntarily submit there, including your GitHub username and report, is visible to others and used to respond to your request. Never post credentials, private server details, or private files.
