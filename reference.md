# Reference
## Auth
<details><summary><code>client.auth.<a href="src/kard/auth/client.py">get_token</a>(...) -&gt; AsyncHttpResponse[TokenResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.get_token(
    client_id="client_id",
    client_secret="client_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/kard/files/client.py">get_metadata</a>(...) -&gt; AsyncHttpResponse[GetFilesMetadataResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves metadata for files associated with a specific issuer/organization.
This endpoint supports pagination and sorting options to efficiently navigate 
through potentially large sets of file metadata.
<b>Required scopes:</b> `files.read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.files.get_metadata(
    organization_id="organization-123",
    page_size=5,
    filter_date_from="2025-02-20T21:56:23Z",
    filter_date_to="2025-03-20T21:56:23Z",
    filter_file_type="earnedRewardApprovedDailyReconciliationFile",
    sort="-sentDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**filter_date_from:** `typing.Optional[str]` — Start date for filtering files (format ISO8601). If not provided, defaults to current date minus 1 month.
    
</dd>
</dl>

<dl>
<dd>

**filter_date_to:** `typing.Optional[str]` — End date for filtering files (format ISO8601). If not provided, defaults to current date.
    
</dd>
</dl>

<dl>
<dd>

**filter_file_type:** `typing.Optional[FileType]` — The document file type.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page. Defaults to 10 if not specified and maximum value allowed 100 items per page.
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor for forward pagination (next page).
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` — Cursor for backward pagination (previous page).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[
    typing.Union[
        FilesMetadataSortOptions, typing.Sequence[FilesMetadataSortOptions]
    ]
]` — If provided, response will be sorted by the specified fields. Defaults to descending sentDate, equivalent to "-sentDate"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">get</a>(...) -&gt; AsyncHttpResponse[SubscriptionsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to fetch the subscriptions of the provided issuer.<br/>
<b>Required scopes:</b> `notifications:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.subscriptions.get(
    organization_id="organization-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**filter_event_name:** `typing.Optional[NotificationType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateSubscriptionsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to subscribe to notification events.<br/>
<b>Required scopes:</b> `notifications:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.notifications.subscriptions import (
    SubscriptionRequestAttributes,
    SubscriptionRequestUnion_Subscription,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.subscriptions.create(
    organization_id="organization-123",
    data=[
        SubscriptionRequestUnion_Subscription(
            attributes=SubscriptionRequestAttributes(
                event_name="earnedRewardApproved",
                webhook_url="https://webhookUrl.com/post",
                enabled=True,
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[SubscriptionRequestUnion]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateSubscriptionsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update existing notification subscriptions.<br/>
<b>Required scopes:</b> `notifications:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.notifications.subscriptions import (
    UpdateSubscriptionRequestAttributes,
    UpdateSubscriptionRequestUnion_Subscription,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.subscriptions.update(
    organization_id="organization-123",
    subscription_id="subscription-123",
    data=UpdateSubscriptionRequestUnion_Subscription(
        attributes=UpdateSubscriptionRequestAttributes(
            event_name="earnedRewardApproved",
            webhook_url="https://webhookUrl.com/post",
            enabled=True,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `SubscriptionId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `UpdateSubscriptionRequestUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ping
<details><summary><code>client.ping.<a href="src/kard/ping/client.py">ping</a>() -&gt; AsyncHttpResponse[PingResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to verify network connectivity and service availability.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.ping.ping()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create</a>(...) -&gt; AsyncHttpResponse[TransactionsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to send all transactions made by all your enrolled users in your rewards program. The request body will depend on the transaction type.<br/>
Please use the correct type when calling the endpoint:
- `transaction`: These incoming transactions will be processed and matched by the Kard system. Learn more about the [Transaction CLO Matching](https://github.com/kard-financial/kard-postman#c-transaction-clo-matching) flow here.
- `matchedTransaction`: For pre-matched transactions that need validation on match by the Kard system.
- `coreTransaction`: For transactions from core banking systems with limited card-level data.<br/>

<b>Required scopes:</b> `transaction:write`<br/>
<b>Note:</b> `Maximum of 500 transactions can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from kard import KardApi
from kard.transactions import (
    CoreTransactionAttributes,
    Transactions_CoreTransaction,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.transactions.create(
    organization_id="organization-123",
    data=[
        Transactions_CoreTransaction(
            id="core_txn_98765432109876543210",
            attributes=CoreTransactionAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                transaction_id="CORE-TXN-2024-001234",
                amount=4599,
                currency="USD",
                description="WALMART SUPERCENTER",
                direction="DEBIT",
                settled_date=datetime.datetime.fromisoformat(
                    "2024-10-15 14:30:00+00:00",
                ),
                authorization_date=datetime.datetime.fromisoformat(
                    "2024-10-15 14:25:00+00:00",
                ),
                financial_institution_name="First National Bank",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[Transactions]` 

Discriminated union representing the request body for submitting a transaction.
Use `type` to distinguish between the two:
- `transaction`: For transactions requiring processing and matching by the Kard system.
- `matchedTransaction`: For pre-matched transactions that need validation on match by the Kard system.
- `coreTransaction`: For transactions from core banking systems with limited card-level data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_fraud_markers</a>(...) -&gt; AsyncHttpResponse[FraudulentTransactionObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to flag a submitted transaction as fraudulent. This will prevent it from being rewarded.<br/>

<b>Required scopes:</b>&nbsp;&nbsp;`transaction:write`<br/>
<b>Note:</b> `Maximum of 500 fraudulent transactions can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.transactions import (
    FraudulentTransactionAttributes,
    FraudulentTransactionData,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.transactions.create_fraud_markers(
    organization_id="organization-123",
    data=[
        FraudulentTransactionData(
            id="myTxnId12345",
            type="fraudulentTransaction",
            attributes=FraudulentTransactionAttributes(
                user_id="userId123",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[FraudulentTransactionData]` — List of fraudulent transactions to report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_audits</a>(...) -&gt; AsyncHttpResponse[CreateAuditResponseBody]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to request that a particular transaction be audited further by the Kard system, in the event of a missing cashback claim, incorrect cashback amount claim or other mis-match claims.<br/>
<b>Required scopes:</b> `audit:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.transactions import AuditAttributes, CreateAuditRequestDataUnion_Audit

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.transactions.create_audits(
    organization_id="organization-123",
    user_id="user-123",
    data=[
        CreateAuditRequestDataUnion_Audit(
            attributes=AuditAttributes(
                audit_code=8001,
                merchant_name="Caribbean Goodness",
                audit_description="duplicate transaction",
                transaction_id="issuerTransaction123",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[CreateAuditRequestDataUnion]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">get_earned_rewards</a>(...) -&gt; AsyncHttpResponse[GetEarnedRewardsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve rewarded transaction history for a specific user. Returns only SETTLED transactions within the last 12 months.
<br/>
<b>Required scopes:</b> `transaction:read`
<br/>
<b>Query Limit:</b> Maximum of 12 months of transaction data can be queried.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.transactions.get_earned_rewards(
    organization_id="org-123",
    user_id="user-456",
    page_size=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor for next page (base64-encoded timestamp + transaction ID)
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` — Cursor for previous page (base64-encoded timestamp + transaction ID)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/kard/users/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateUsersObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to enroll a specified user into your rewards program.<br/>

<b>Required scopes:</b>&nbsp;&nbsp;`user:write`<br/>
<b>Note:</b> `Maximum of 100 users can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.users import UserRequestAttributes, UserRequestDataUnion_User

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.create(
    organization_id="organization-123",
    data=[
        UserRequestDataUnion_User(
            id="1234567890",
            attributes=UserRequestAttributes(
                zip_code="11238",
                enrolled_rewards=["CARDLINKED"],
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[UserRequestDataUnion]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateUserObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update the details on a specified user.<br/>

<b>Required scopes:</b> `user:update`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.users import UserRequestAttributes, UserRequestDataUnion_User

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.update(
    organization_id="organization-123",
    user_id="user-123",
    data=UserRequestDataUnion_User(
        id="1234567890",
        attributes=UserRequestAttributes(
            zip_code="11238",
            enrolled_rewards=["CARDLINKED"],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `UserRequestDataUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">delete</a>(...) -&gt; AsyncHttpResponse[DeleteUserResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to delete a specified enrolled user from the rewards program and Kard's system. Users can be re-enrolled into rewards by calling the [Create User](/2024-10-01/api/users/create) endpoint using the same `id` from before.<br/>

<b>Required scopes:</b> `user:delete`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.delete(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">get</a>(...) -&gt; AsyncHttpResponse[UpdateUserObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to fetch the details on a specified user.<br/>
<br/>
<b>Required scopes:</b>&nbsp;&nbsp;`user:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.get(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Attributions
<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateAttributionResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to send attribution events made by a single enrolled user for processing. A maximum of 100 events can be included in a single request.

<b>Required scopes:</b> `attributions:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from kard import KardApi
from kard.users.attributions import (
    CreateAttributionRequestUnion_NotificationAttribution,
    CreateAttributionRequestUnion_OfferAttribution,
    NotificationAttributionAttributes,
    OfferAttributionAttributes,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.attributions.create(
    organization_id="organization-123",
    user_id="user-123",
    data=[
        CreateAttributionRequestUnion_OfferAttribution(
            attributes=OfferAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c075",
                event_code="VIEW",
                medium="SEARCH",
                event_date=datetime.datetime.fromisoformat(
                    "2025-01-01 00:00:00+00:00",
                ),
            ),
        ),
        CreateAttributionRequestUnion_OfferAttribution(
            attributes=OfferAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c077",
                event_code="IMPRESSION",
                medium="EMAIL",
                event_date=datetime.datetime.fromisoformat(
                    "2025-01-01 00:00:00+00:00",
                ),
            ),
        ),
        CreateAttributionRequestUnion_NotificationAttribution(
            attributes=NotificationAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c076",
                event_code="IMPRESSION",
                medium="PUSH",
                event_date=datetime.datetime.fromisoformat(
                    "2025-01-01 00:00:00+00:00",
                ),
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[CreateAttributionRequestUnion]` 

Discriminated union representing the request body for submitting attribution events.
Use `type` to distinguish between the two:
- `offerAttribution`: Events related to viewing or interacting with an offer.
- `notificationAttribution`: Events related to viewing or interacting with a notification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">activate</a>(...) -&gt; AsyncHttpResponse[ActivateOfferResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record when a user activates an offer. Creates an attribution event with eventCode=ACTIVATE and medium=CTA.
Optionally include the offer data by passing `include=offer`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.attributions.activate(
    organization_id="organization-123",
    user_id="user-123",
    offer_id="offer-456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**offer_id:** `str` — The unique identifier of the offer being activated
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the offer response (when include=offer).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[
    typing.Union[
        ActivateOfferIncludeOption, typing.Sequence[ActivateOfferIncludeOption]
    ]
]` — Related resources to include in the response. Allowed value is `offer`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WebView
<details><summary><code>client.users.auth.<a href="src/kard/users/auth/client.py">get_web_view_token</a>(...) -&gt; AsyncHttpResponse[WebViewTokenResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an OAuth token for webview authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.auth.get_web_view_token(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rewards
<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">offers</a>(...) -&gt; AsyncHttpResponse[OffersResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national brand offers that a specified user is eligible for. Call this endpoint to build out your
[targeted offers UX experience](/2024-10-01/api/getting-started#b-discover-a-lapsed-customer-clo). Local offers details
can be found by calling the [Get Eligible Locations](/2024-10-01/api/rewards/locations).<br/>
<b>Required scopes:</b> `rewards:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.rewards.offers(
    organization_id="organization-123",
    user_id="user-123",
    page_size=1,
    filter_is_targeted=True,
    sort="-startDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_purchase_channel:** `typing.Optional[typing.Sequence[PurchaseChannel]]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[CategoryOption]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_is_targeted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[
    typing.Union[OfferSortOptions, typing.Sequence[OfferSortOptions]]
]` — If provided, response will be sorted by the specified fields
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — CSV list of included resources in the response (e.g "categories"). Allowed value is `categories`.
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the response. Valid values are shortDescription, longDescription, cta, tags, and detailTags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">locations</a>(...) -&gt; AsyncHttpResponse[LocationsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national and local geographic locations that a specified user has eligible in-store offers at. Use this endpoint to build
out your [map-specific UX experiences](/2024-10-01/api/getting-started#c-discover-clos-near-you-map-view). Please note
that Longitude and Latitude fields are prioritized over State, City and Zipcode and are the recommended search
pattern.<br/>
<br/>
<b>Required scopes:</b> `rewards:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.rewards.locations(
    organization_id="organization-123",
    user_id="user-123",
    page_size=1,
    filter_latitude=39.9419429,
    filter_longitude=-75.1446869,
    filter_radius=10,
    include="offers,categories",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_zip_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_state:** `typing.Optional[State]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[CategoryOption]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[
    typing.Union[LocationSortOptions, typing.Sequence[LocationSortOptions]]
]` — If provided, response will be sorted by the specified fields
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — CSV list of included resources in the response (e.g "offers,categories"). Allowed values are `offers` and `categories`.
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in included offers. Valid values are shortDescription, longDescription, cta, tags, and detailTags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Uploads
<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateUploadResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to create an upload session and retrieve an upload ID. Using the upload ID in the [Add Upload 
Part](/api/uploads/create-upload-part) endpoint, historical transactions can be sent in batches for further processing.
<b>Required scopes:</b> `transaction:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.commons import EmptyObject
from kard.users.uploads import (
    CreateUploadRequestDataUnion_HistoricalTransactionStart,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.uploads.create(
    organization_id="organization-123",
    user_id="user-123",
    data=CreateUploadRequestDataUnion_HistoricalTransactionStart(
        attributes=EmptyObject(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**data:** `CreateUploadRequestDataUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create_part</a>(...) -&gt; AsyncHttpResponse[CreateUploadPartResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint using the upload ID provided in the [Create Upload](/api/uploads/create-upload) endpoint to add parts to your upload. Currently, this endpoint supports adding historical transactions.
<b>Required scopes:</b> `transaction:write`
<b>Note:</b> `Maximum of 500 transactions can be uploaded per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from kard import KardApi
from kard.transactions import Merchant, TransactionsAttributes
from kard.users.uploads import CreateUploadPartDataUnion_HistoricalTransaction

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.uploads.create_part(
    organization_id="organization-123",
    user_id="user-123",
    upload_id="upload-123",
    data=[
        CreateUploadPartDataUnion_HistoricalTransaction(
            id="309rjfoincor3icno3rind093cdow3jciwjdwcm",
            attributes=TransactionsAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                status="APPROVED",
                amount=1000,
                subtotal=800,
                currency="USD",
                direction="DEBIT",
                payment_type="CARD",
                description="ADVANCEAUTO",
                description_2="ADVANCEAUTO",
                mcc="1234",
                card_bin="123456",
                card_last_four="4321",
                authorization_date=datetime.datetime.fromisoformat(
                    "2021-07-02 17:47:06+00:00",
                ),
                merchant=Merchant(
                    id="12345678901234567",
                    name="ADVANCEAUTO",
                    addr_street="125 Main St",
                    addr_city="Philadelphia",
                    addr_state="PA",
                    addr_zipcode="19147",
                    addr_country="United States",
                    latitude="37.9419429",
                    longitude="-73.1446869",
                    store_id="12345",
                ),
                authorization_code="123456",
                retrieval_reference_number="100804333919",
                acquirer_reference_number="1234567890123456789012345678",
                system_trace_audit_number="333828",
                transaction_id="2467de37-cbdc-416d-a359-75de87bfffb0",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload ID identifying the upload session to add parts
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[CreateUploadPartDataUnion]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateUploadResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update your upload session. Currently, you can signal completing a historical transactions upload.
<b>Required scopes:</b> `transaction:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.commons import EmptyObject
from kard.users.uploads import (
    UpdateUploadRequestDataUnion_HistoricalTransactionComplete,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.uploads.update(
    organization_id="organization-123",
    user_id="user-123",
    upload_id="upload-123",
    data=UpdateUploadRequestDataUnion_HistoricalTransactionComplete(
        id="7e382223-b9a5-4825-91fb-436c8957a2e7",
        attributes=EmptyObject(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload ID identifying the upload session to update

</dd>
</dl>

<dl>
<dd>

**data:** `UpdateUploadRequestDataUnion`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## HEM
<details><summary><code><a href="src/kard/hem.py">generate_hem</a>(raw) -&gt; str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a Hashed Email (HEM) from a raw email address. The email is normalized
following UID2/LiveRamp industry standards before being hashed with SHA-256.

Normalization rules:
- Remove all whitespace
- Lowercase the entire address
- Gmail/Googlemail only: remove dots from local-part, strip '+' suffix
- Canonicalize googlemail.com to gmail.com
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard.hem import generate_hem

hem = generate_hem("Test.User+extra@gmail.com")
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `str` — The raw email address to normalize and hash.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

