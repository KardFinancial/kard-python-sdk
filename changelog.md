## 0.1.0 - 2026-01-27
* feat: add webview authentication support for users
* Introduce comprehensive webview authentication functionality to enable OAuth token generation for user webviews. This provides a secure mechanism for authenticating users within embedded webview contexts.
* Key changes:
* Add new auth client with get_webview_token endpoint for retrieving OAuth tokens
* Implement WebviewTokenResponse model with access_token, expires_in, and token_type fields
* Add auth submodule to users namespace with both sync and async client support
* Update documentation with usage examples and parameter descriptions
* Integrate auth client as property of UsersClient and AsyncUsersClient
* 🌿 Generated with Fern

