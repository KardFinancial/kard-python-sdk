# Reference
## Attributions
<details><summary><code>client.attributions.<a href="src/kard/attributions/client.py">internal_bulk_create_attributions</a>(...) -> AsyncHttpResponse[InternalBulkCreateAttributionsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to persist attribution events. A maximum of 100 events can be included in a single request.
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
from kard.attributions import (
    InternalApiAttribution_OfferAttribution,
    InternalApiOfferAttributionAttributes,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.attributions.internal_bulk_create_attributions(
    data=[
        InternalApiAttribution_OfferAttribution(
            attributes=InternalApiOfferAttributionAttributes(
                issuer_id="issuerId",
                user_id="userId",
                entity_id="entityId",
                event_code="IMPRESSION",
                medium="BROWSE",
                event_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            ),
        ),
        InternalApiAttribution_OfferAttribution(
            attributes=InternalApiOfferAttributionAttributes(
                issuer_id="issuerId",
                user_id="userId",
                entity_id="entityId",
                event_code="IMPRESSION",
                medium="BROWSE",
                event_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
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

**data:** `typing.Sequence[InternalApiAttribution]` 
    
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

<details><summary><code>client.attributions.<a href="src/kard/attributions/client.py">internal_get_attributions</a>(...) -> AsyncHttpResponse[InternalGetAttributionsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of attribution records with optional filtering and pagination.
Returns attribution events that match the specified criteria.
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
client.attributions.internal_get_attributions(
    organization_id="organizationId",
    user_id="userId",
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

**filter_type:** `typing.Optional[InternalAttributionType]` — Filter by attribution type (offerAttribution or notificationAttribution)
    
</dd>
</dl>

<dl>
<dd>

**filter_entity_id:** `typing.Optional[str]` — Filter by entity ID
    
</dd>
</dl>

<dl>
<dd>

**filter_event_code:** `typing.Optional[InternalEventCode]` — Filter by event code (IMPRESSION or VIEW)
    
</dd>
</dl>

<dl>
<dd>

**filter_start_date:** `typing.Optional[dt.datetime]` — Filter attributions after this date (ISO 8601 format)
    
</dd>
</dl>

<dl>
<dd>

**filter_end_date:** `typing.Optional[dt.datetime]` — Filter attributions before this date (ISO 8601 format)
    
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

**page_size:** `typing.Optional[int]` — Number of items per page. Defaults to 10 if not specified and maximum value allowed 100 items per page.
    
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

## Auth
<details><summary><code>client.auth.<a href="src/kard/auth/client.py">get_token</a>(...) -> AsyncHttpResponse[TokenResponse]</code></summary>
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

## BillingAgent
<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">create_issuer_reward</a>(...) -> AsyncHttpResponse[CreateIssuerRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to create a new reward entry in the ledger.<br/>
<b>Required scopes:</b> `reward:write`
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
client.billing_agent.create_issuer_reward(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    transaction_ids=["billing.TransactionId.Sample"],
    description="Reward payout for transaction",
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**transaction_ids:** `typing.Sequence[TransactionId]` — TransactionIds is a list of transactions related to the reward payout
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payout
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">revert_issuer_reward</a>(...) -> AsyncHttpResponse[RevertIssuerRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to revert a reward for the issuer
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_agent.revert_issuer_reward(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    reward_id=uuid.UUID(
        "82ed6e40-f2f6-4f66-be17-52c03ad64414",
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `RewardId` — ID of the reward entry
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">get_issuer_reward</a>(...) -> AsyncHttpResponse[GetIssuerRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to get a reward.<br/>
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_agent.get_issuer_reward(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    reward_id=uuid.UUID(
        "82ed6e40-f2f6-4f66-be17-52c03ad64414",
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `RewardId` — ID of the reward entry
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Optional[bool]` — Include reward entries in the response
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">get_issuer_rewards</a>(...) -> AsyncHttpResponse[GetIssuerRewardsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to list rewards. MUST BE FILTERED<br/>
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
client.billing_agent.get_issuer_rewards(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[RewardsFilterOptions]` 
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">get_issuer_matched_transaction_info</a>(...) -> AsyncHttpResponse[GetIssuerMatchedTransactionInfoResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to get information on a list of matched transactions
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
client.billing_agent.get_issuer_matched_transaction_info(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    transaction_ids="123456,876543",
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**transaction_ids:** `str` — Comma-separated list of transactions IDs to fetch info for
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">eom_updates</a>(...) -> AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to get information on a list of matched transactions
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
from kard.billing_agent import EomUpdatePayload

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_agent.eom_updates(
    issuer_id="issuerId",
    data=[
        EomUpdatePayload(
            id="id",
            attributes={"attributes": {"key": "value"}},
        ),
        EomUpdatePayload(
            id="id",
            attributes={"attributes": {"key": "value"}},
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[EomUpdatePayload]` 
    
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

<details><summary><code>client.billing_agent.<a href="src/kard/billing_agent/client.py">update_matched_transaction</a>(...) -> AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update a matched transaction with adjusted commission
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
from kard.billing_agent import UpdateMatchedTransactionPayload

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_agent.update_matched_transaction(
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    transaction_id="123456",
    data=UpdateMatchedTransactionPayload(
        issuer_amount=100,
        cardholder_amount=100,
        kard_fee=100,
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

**issuer_id:** `IssuerId` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — The ID of the user
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `TransactionId` — The ID of the transaction
    
</dd>
</dl>

<dl>
<dd>

**data:** `UpdateMatchedTransactionPayload` 
    
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

## BillingService
<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">create_reward</a>(...) -> AsyncHttpResponse[CreateRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to create a new reward entry in the ledger.<br/>
<b>Required scopes:</b> `rewards:write`
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
client.billing_service.create_reward(
    transaction_ids=["5e27318c9b346f00087fbb32"],
    issuer_id="5e27318c9b346f00087fbb32",
    user_id="5e27318c9b346f00087fbb32",
    description="Reward payout for transaction",
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

**transaction_ids:** `typing.Sequence[TransactionId]` — TransactionIds is a list of transactions related to the reward payout
    
</dd>
</dl>

<dl>
<dd>

**issuer_id:** `IssuerId` — ID of the issuer associated with the reward
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` — ID of the user associated with the rewards
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payout
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">get_reward</a>(...) -> AsyncHttpResponse[GetRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to get a reward by its ID.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_service.get_reward(
    reward_id=uuid.UUID(
        "abd6e578-d130-44e6-bf4b-8dddb31038b0",
    ),
    entries=True,
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

**reward_id:** `RewardId` — ID of the reward entry
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Optional[bool]` — Include reward entries in the response
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">get_rewards</a>(...) -> AsyncHttpResponse[GetRewardsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to list rewards. MUST BE FILTERED<br/>
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
client.billing_service.get_rewards()

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

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[RewardsFilterOptions]` 
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">get_reward_entries</a>(...) -> AsyncHttpResponse[GetRewardEntriesResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to list reward entries.<br/>
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
client.billing_service.get_reward_entries()

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

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[RewardsFilterOptions]` 
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">update_reward</a>(...) -> AsyncHttpResponse[UpdateRewardResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to create an adjustment entry in the ledger for a reward.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_service.update_reward(
    reward_id=uuid.UUID(
        "abd6e578-d130-44e6-bf4b-8dddb31038b0",
    ),
    issuer_amount=0,
    card_holder_amount=0,
    kard_fees=-50,
    description="Waive fees for transaction",
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

**reward_id:** `RewardId` — ID of the reward entry
    
</dd>
</dl>

<dl>
<dd>

**issuer_amount:** `int` — Amount in cents to the Issuer
    
</dd>
</dl>

<dl>
<dd>

**card_holder_amount:** `int` — Amount in cents to the Card Holder
    
</dd>
</dl>

<dl>
<dd>

**kard_fees:** `int` — Amount in cents of the Kard fees
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payout
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">revert_reward</a>(...) -> AsyncHttpResponse[RevertRewardsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to revert a reward
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_service.revert_reward(
    reward_id=uuid.UUID(
        "82ed6e40-f2f6-4f66-be17-52c03ad64414",
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

**reward_id:** `RewardId` — ID of the reward entry
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">revert_rewards</a>(...) -> AsyncHttpResponse[RevertRewardsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to revert rewards
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
client.billing_service.revert_rewards()

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

**filter:** `typing.Optional[RewardsFilterOptions]` 
    
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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">upload_invoice_status</a>() -> AsyncHttpResponse[InvoiceStatusFileResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint get a presigned URL that can be used to upload the EOM invoice status file.
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
client.billing_service.upload_invoice_status()

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

<details><summary><code>client.billing_service.<a href="src/kard/billing_service/client.py">trigger_merchant_invoice</a>(...) -> AsyncHttpResponse[TriggerMerchantInvoiceResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers the job to issue a merchant invoice
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

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_service.trigger_merchant_invoice(
    merchant_id="merchantId",
    start_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**merchant_id:** `MerchantId` — ID of the reward entry
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `dt.datetime` — RFC3339 time indicating the start of the billing period (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `dt.datetime` — RFC3339 time indicating the end of the billing period (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**invoice_name:** `typing.Optional[str]` — optional name for the invoice. If none is provided, one will be generated.
    
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

## Eligibility-Broker
<details><summary><code>client.eligibility_broker.<a href="src/kard/eligibility_broker/client.py">ingest</a>(...) -> AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send events to be ingested by the eligibility broker to change a user's eligibility.
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
from kard.eligibility_broker import (
    IngestionEvents_SegmentUser,
    SegmentationIngestionEventAttributes,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility_broker.ingest(
    data=[
        IngestionEvents_SegmentUser(
            attributes=SegmentationIngestionEventAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                issuer_id="00073100",
                segment_id="5eb2d4a39ce24e00081488c4",
                status="ACTIVE",
                event_time=datetime.datetime.fromisoformat(
                    "2021-07-02 17:47:06+00:00",
                ),
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

**data:** `typing.Sequence[IngestionEvents]` 

Discriminated union representing the request body for submitting an eligibility event.
Use `type` to distinguish between the two:
- `segmentUser`: For segmentation events that change eligibility.
    
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

## Experiments
<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">list_experiments</a>(...) -> AsyncHttpResponse[ListExperimentsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A list of experiments.
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
from kard.experiments import ListExperimentsFilter

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.list_experiments(
    filter=ListExperimentsFilter(
        q="some experiment name that doesn't exist",
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

**page:** `typing.Optional[Page]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ListExperimentsFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListExperimentsSort]` 
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">get_experiment_by_id</a>(...) -> AsyncHttpResponse[ExperimentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an experiment by id.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.get_experiment_by_id(
    id=uuid.UUID(
        "3fc40dd7-f74e-40fc-8236-027fb98ae8a5",
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

**id:** `uuid.UUID` — The id of the experiment.
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">create_experiment</a>(...) -> AsyncHttpResponse[ExperimentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an experiment.
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
from kard.experiments import Experiment

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.create_experiment(
    attributes=Experiment(
        name="Experiment 1",
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

**attributes:** `Experiment` 
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">update_experiment</a>(...) -> AsyncHttpResponse[ExperimentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an experiment.
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
import uuid

from kard import KardApi
from kard.experiments import Experiment

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.update_experiment(
    id=uuid.UUID(
        "3fc40dd7-f74e-40fc-8236-027fb98ae8a5",
    ),
    attributes=Experiment(
        name="Experiment 1",
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

**id:** `uuid.UUID` — The id of the experiment.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `Experiment` 
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">create_offer_link</a>(...) -> AsyncHttpResponse[OfferLinkResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an offer link for an experiment.
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
import uuid

from kard import KardApi
from kard.experiments import OfferLinkCompleted

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.create_offer_link(
    attributes=OfferLinkCompleted(
        experiment_id=uuid.UUID(
            "a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
        ),
        offer_id="a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
        rules=[],
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

**attributes:** `OfferLinkUnion` 
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">list_offer_links</a>(...) -> AsyncHttpResponse[ListOfferLinksResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all offer links for an experiment.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.list_offer_links(
    experiment_id=uuid.UUID(
        "3fc40dd7-f74e-40fc-8236-027fb98ae8a5",
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

**experiment_id:** `uuid.UUID` — The id of the experiment.
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">get_offer_link_by_id</a>(...) -> AsyncHttpResponse[OfferLinkResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an offer link by id.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.get_offer_link_by_id(
    id=uuid.UUID(
        "a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
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

**id:** `uuid.UUID` — The id of the offer link.
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">update_offer_link</a>(...) -> AsyncHttpResponse[OfferLinkResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an offer link for an experiment.
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
import uuid

from kard import KardApi
from kard.experiments import OfferLinkCompleted

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.update_offer_link(
    id=uuid.UUID(
        "a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
    ),
    attributes=OfferLinkCompleted(
        experiment_id=uuid.UUID(
            "a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
        ),
        offer_id="a52cd8d3-a6a3-4819-a7e2-8bb5736f8ac8",
        rules=[],
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

**id:** `uuid.UUID` — The id of the offer link.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `OfferLinkUnion` 
    
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

<details><summary><code>client.experiments.<a href="src/kard/experiments/client.py">delete_offer_link</a>(...) -> AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an offer link for an experiment.
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
import uuid

from kard import KardApi

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.experiments.delete_offer_link(
    id=uuid.UUID(
        "3fc40dd7-f74e-40fc-8236-027fb98ae8a5",
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

**id:** `uuid.UUID` — The id of the offer link.
    
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
<details><summary><code>client.files.<a href="src/kard/files/client.py">internal_save_file</a>(...) -> AsyncHttpResponse[SaveFilesMetadataResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to save conciliation file metadata.
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
from kard.commons import RelationshipData, RelationshipSingle
from kard.files import FileMetadataAttributesResource, FileMetadataResource

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.files.internal_save_file(
    organization_id="organizationId",
    data=[
        FileMetadataResource(
            id="id",
            type="earnedRewardApprovedDailyReconciliationFile",
            attributes=FileMetadataAttributesResource(
                file_name="fileName",
                bucket_name="bucketName",
                last_modified="lastModified",
                sent_at="sentAt",
            ),
            relationships={
                "relationships": RelationshipSingle(
                    data=RelationshipData(
                        type="type",
                        id="id",
                    ),
                )
            },
        ),
        FileMetadataResource(
            id="id",
            type="earnedRewardApprovedDailyReconciliationFile",
            attributes=FileMetadataAttributesResource(
                file_name="fileName",
                bucket_name="bucketName",
                last_modified="lastModified",
                sent_at="sentAt",
            ),
            relationships={
                "relationships": RelationshipSingle(
                    data=RelationshipData(
                        type="type",
                        id="id",
                    ),
                )
            },
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

**data:** `typing.Sequence[FileMetadataResource]` 
    
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

<details><summary><code>client.files.<a href="src/kard/files/client.py">get_metadata</a>(...) -> AsyncHttpResponse[GetFilesMetadataResponse]</code></summary>
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
<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">get</a>(...) -> AsyncHttpResponse[SubscriptionsResponseObject]</code></summary>
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

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">create</a>(...) -> AsyncHttpResponse[CreateSubscriptionsResponseObject]</code></summary>
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

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">update</a>(...) -> AsyncHttpResponse[UpdateSubscriptionsResponseObject]</code></summary>
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

## Offers
<details><summary><code>client.offers.<a href="src/kard/offers/client.py">get_offers</a>(...) -> AsyncHttpResponse[OffersListResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get offers
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
client.offers.get_offers()

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

**page_after:** `typing.Optional[str]` — Represents a cursor value, and if provided, returns the next page of results
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` — Represents a cursor value, and if provided, returns the previous page of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Maximum number of records to be returned [1 - 200], (default = 200)
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Comma-separated list of related resources to include (e.g., merchant,locations,segments,audiences)
    
</dd>
</dl>

<dl>
<dd>

**filter_name:** `typing.Optional[str]` — Filter by offer name
    
</dd>
</dl>

<dl>
<dd>

**filter_offer_type:** `typing.Optional[LocationType]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_merchant_id:** `typing.Optional[str]` — Filter by merchant ID
    
</dd>
</dl>

<dl>
<dd>

**filter_start_date:** `typing.Optional[str]` — Filter by start date (ISO 8601 format)
    
</dd>
</dl>

<dl>
<dd>

**filter_expiration_date:** `typing.Optional[str]` — Filter by expiration date (ISO 8601 format)
    
</dd>
</dl>

<dl>
<dd>

**filter_source:** `typing.Optional[Source]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[str]` — Filter by offer category
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[Status]` — Filter by offer status
    
</dd>
</dl>

<dl>
<dd>

**filter_id:** `typing.Optional[str]` — Filter by id
    
</dd>
</dl>

<dl>
<dd>

**filter_is_targeted:** `typing.Optional[bool]` — Filter by isTargeted
    
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

<details><summary><code>client.offers.<a href="src/kard/offers/client.py">get_offer_by_id</a>(...) -> AsyncHttpResponse[OfferResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific offer by ID
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
client.offers.get_offer_by_id(
    offer_id="offerId",
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

**offer_id:** `str` — Unique identifier of the offer
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Comma-separated list of related resources to include
    
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

<details><summary><code>client.offers.<a href="src/kard/offers/client.py">create_offer</a>(...) -> AsyncHttpResponse[OfferResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new offer
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
from kard.offers import (
    Attribution,
    CreateOfferRequestAttributes,
    CreateOfferRequestData,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.offers.create_offer(
    data=CreateOfferRequestData(
        attributes=CreateOfferRequestAttributes(
            name="name",
            merchant_id="merchantId",
            offer_type="INSTORE",
            is_location_specific=True,
            status="INACTIVE",
            merchant_network="merchantNetwork",
            opt_in_required=True,
            qualified_issuer=["qualifiedIssuer", "qualifiedIssuer"],
            commission_type="FLAT",
            commission_value=1.1,
            issuer_commissions_map={"issuerCommissionsMap": 1.1},
            start_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            expiration_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            redeemable_once=True,
            source="NATIONAL",
            attribution=Attribution(
                is_required=True,
                events=["IMPRESSION", "IMPRESSION"],
            ),
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

**data:** `CreateOfferRequestData` — Offer data for creation
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[OfferRequestMeta]` — Metadata for the offer creation request
    
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

<details><summary><code>client.offers.<a href="src/kard/offers/client.py">update_offer</a>(...) -> AsyncHttpResponse[OfferResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing offer (replaces all fields - omitted optional fields will be removed)
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
from kard.offers import (
    Attribution,
    UpdateOfferRequestAttributes,
    UpdateOfferRequestData,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.offers.update_offer(
    offer_id="offerId",
    data=UpdateOfferRequestData(
        attributes=UpdateOfferRequestAttributes(
            name="name",
            merchant_id="merchantId",
            offer_type="INSTORE",
            is_location_specific=True,
            status="INACTIVE",
            merchant_network="merchantNetwork",
            opt_in_required=True,
            qualified_issuer=["qualifiedIssuer", "qualifiedIssuer"],
            commission_type="FLAT",
            commission_value=1.1,
            issuer_commissions_map={"issuerCommissionsMap": 1.1},
            start_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            expiration_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            redeemable_once=True,
            source="NATIONAL",
            attribution=Attribution(
                is_required=True,
                events=["IMPRESSION", "IMPRESSION"],
            ),
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

**offer_id:** `str` — Unique identifier of the offer to update
    
</dd>
</dl>

<dl>
<dd>

**data:** `UpdateOfferRequestData` — Offer data for update
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[OfferRequestMeta]` — Metadata for the offer update request
    
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
<details><summary><code>client.ping.<a href="src/kard/ping/client.py">ping</a>() -> AsyncHttpResponse[PingResponseObject]</code></summary>
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

## Queue Dispatcher
<details><summary><code>client.queue_dispatcher.<a href="src/kard/queue_dispatcher/client.py">dispatch_event</a>(...) -> AsyncHttpResponse[GenericNotificationResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to dispatch an event to the notifications service queue.<br/>
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
from kard.commons import RelationshipData, RelationshipSingle
from kard.queue_dispatcher import NotificationResource

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.queue_dispatcher.dispatch_event(
    organization_id="organizationId",
    issuer_name="issuerName",
    x_kard_issuer_id="X-Kard-IssuerID",
    data=[
        NotificationResource(
            id="id",
            type="type",
            attributes={"attributes": {"key": "value"}},
            relationships={
                "relationships": RelationshipSingle(
                    data=RelationshipData(
                        type="type",
                        id="id",
                    ),
                )
            },
        ),
        NotificationResource(
            id="id",
            type="type",
            attributes={"attributes": {"key": "value"}},
            relationships={
                "relationships": RelationshipSingle(
                    data=RelationshipData(
                        type="type",
                        id="id",
                    ),
                )
            },
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

**issuer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**x_kard_issuer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[NotificationResource]` 
    
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

## SegmentUsers
<details><summary><code>client.segment_users.<a href="src/kard/segment_users/client.py">get_status</a>(...) -> AsyncHttpResponse[GetStatusResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if a user is in a segment
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
client.segment_users.get_status(
    issuer_id="issuerId",
    referring_partner_user_id="referringPartnerUserId",
    segment_ids=["segmentIds", "segmentIds"],
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

**issuer_id:** `str` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**referring_partner_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**segment_ids:** `typing.Sequence[str]` — A list of segmentIds
    
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

<details><summary><code>client.segment_users.<a href="src/kard/segment_users/client.py">get_statuses</a>(...) -> AsyncHttpResponse[GetStatusesResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if users are in segments
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
client.segment_users.get_statuses(
    issuer_id="issuerId",
    referring_partner_user_ids=[
        "referringPartnerUserIds",
        "referringPartnerUserIds",
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

**issuer_id:** `str` — The id of the issuer
    
</dd>
</dl>

<dl>
<dd>

**referring_partner_user_ids:** `typing.Sequence[str]` — A list of referring partner user IDs
    
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

## Transactions
<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create</a>(...) -> AsyncHttpResponse[TransactionsResponse]</code></summary>
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
- `matchedTransaction`: For pre-matched transactions that need validation on match by the Kard system.<br/>

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
    MatchedTransactionsAttributes,
    Merchant,
    Transactions_MatchedTransaction,
)

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.transactions.create(
    organization_id="organization-123",
    data=[
        Transactions_MatchedTransaction(
            id="unknown_payment_txn_12345",
            attributes=MatchedTransactionsAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                amount=2500,
                subtotal=2000,
                description="ONLINE STORE PURCHASE",
                authorization_date=datetime.datetime.fromisoformat(
                    "2021-07-02 17:47:06+00:00",
                ),
                payment_type="UNKNOWN",
                matched_offer_id="5eb2d4a39ce24e00081488c4",
                direction="DEBIT",
                merchant=Merchant(
                    id="98765432109876543",
                    name="ONLINE STORE",
                    addr_street="456 Web St",
                    addr_city="Online City",
                    addr_state="CA",
                    addr_zipcode="90210",
                    addr_country="United States",
                ),
                card_last_four="7890",
                authorization_code="5678",
                retrieval_reference_number="200804333919",
                system_trace_audit_number="444939",
                acquirer_reference_number="9876543210987654321098765432",
                transaction_id="unknown-txn-4567-efgh-ijkl-mnop-qrstuvwxyz01",
                order_id="online_order_789012",
                receipt_medium="ELECTRONIC",
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

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_fraud_markers</a>(...) -> AsyncHttpResponse[FraudulentTransactionObject]</code></summary>
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

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_audits</a>(...) -> AsyncHttpResponse[CreateAuditResponseBody]</code></summary>
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

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">get_earned_rewards</a>(...) -> AsyncHttpResponse[GetEarnedRewardsResponse]</code></summary>
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

## TxnMapService
<details><summary><code>client.txn_map_service.<a href="src/kard/txn_map_service/client.py">delete_txn_map</a>(...) -> AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to delete one or many transaction maps entry.
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
from kard.txn_map_service import DeleteTxnData

client = KardApi(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.txn_map_service.delete_txn_map(
    data=[
        DeleteTxnData(
            id="id",
        ),
        DeleteTxnData(
            id="id",
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

**data:** `typing.Sequence[DeleteTxnData]` 
    
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
<details><summary><code>client.users.<a href="src/kard/users/client.py">create</a>(...) -> AsyncHttpResponse[CreateUsersObject]</code></summary>
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

<details><summary><code>client.users.<a href="src/kard/users/client.py">update</a>(...) -> AsyncHttpResponse[UpdateUserObject]</code></summary>
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

<details><summary><code>client.users.<a href="src/kard/users/client.py">delete</a>(...) -> AsyncHttpResponse[DeleteUserResponseObject]</code></summary>
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

<details><summary><code>client.users.<a href="src/kard/users/client.py">get</a>(...) -> AsyncHttpResponse[UpdateUserObject]</code></summary>
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
<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">create</a>(...) -> AsyncHttpResponse[CreateAttributionResponse]</code></summary>
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

## Rewards
<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">offers</a>(...) -> AsyncHttpResponse[OffersResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national brand offers that a specified user is eligible for. Call this endpoint to build out your
[targeted offers UX experience](/2024-10-01/api/getting-started#b-discover-a-lapsed-customer-clo). Local offers details
can be found by calling the [Get Eligible Locations](/2024-10-01/api/rewards/locations) endpoint with the
`includeLocal` query parameter.<br/>
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">locations</a>(...) -> AsyncHttpResponse[LocationsResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national and local geographic locations that a specified user has eligible in-store offers at. To
include local locations, add the `includeLocal` query parameter to your api call. Use this endpoint to build
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Uploads
<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create</a>(...) -> AsyncHttpResponse[CreateUploadResponseObject]</code></summary>
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

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create_part</a>(...) -> AsyncHttpResponse[CreateUploadPartResponseObject]</code></summary>
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

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">update</a>(...) -> AsyncHttpResponse[UpdateUploadResponseObject]</code></summary>
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

