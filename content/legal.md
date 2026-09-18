# Third-party licenses & relinking materials

Corresponding decoder sources, build instructions, notices and library replacement
materials for RemoteFS. The RemoteFS application source repository remains private.

## Downloads

[Source and relinking downloads](downloads.html). Choose materials matching your application from Releases. Unchanged dependencies use the existing shared materials.

## Library Modification

The LGPL-covered libraries are supplied under their included LGPL-2.1-or-later
licenses. Their complete corresponding source archive includes the selected
dependency sources, modifications, notices and reconstruction helpers. Other
components retain their own included licenses and attribution.

For application recipients, the included RemoteFS application object files and
resources may be used to modify the library and relink the application for the
recipient's own use. Reverse engineering of the application for debugging those
library modifications is permitted. No application license restriction is intended
to limit rights granted by the included open-source licenses. These permissions
do not relicense RemoteFS's private source code or grant rights to Apple SDKs,
signing credentials or unrelated third-party material.

Read the README inside each kit. Use your own Apple development tools and signing
access for a physical device. No signing key, provisioning profile, account,
password, customer file or private NAS information is supplied. Do not disable
platform security protections to install a modified application.

## Verification And Support

The source reconstruction and replacement-library relinking workflows were tested
on macOS with Xcode 26.6. Device output is unsigned; simulator installation is
tested separately and is not proof of physical-device installation. See each
release's verification notes for exact scope and limitations.

[RemoteFS support](https://moonight-studio.github.io/RemoteFS/support.html). Issues in this
repository may also be used to report missing or corrupt delivery materials.
Do not post server passwords or private files in an issue.

## 中文

这里提供 RemoteFS 解码库的对应源码、修改、构建说明、许可，以及对应版本应用的
目标文件和重链接工具。RemoteFS 主项目源码不公开。请下载与你安装的应用平台、
版本和构建号一致的材料。你可以为自己使用修改解码库并重新链接应用，也可以为
调试这些修改进行必要的逆向工程。第三方组件仍适用各自的许可条款。

## Component licenses

- [iOS third-party licenses](licenses-ios.html)
- [macOS third-party licenses](licenses-macos.html)

These catalogs change when dependencies or license terms change. Exact historical
inventories are included in their matching relinking archives. Unchanged source,
license and framework materials are shared across application builds.
