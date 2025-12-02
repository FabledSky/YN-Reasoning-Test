# Minimal Item API Sketch

This draft outline shows how a lightweight HTTP API could deliver single-sentence True/False items and collect responses. Adjust payloads as you add metadata (e.g., difficulty or tags).

## Endpoints

### `GET /next_item`
Returns the next available item to present.

```json
{
  "id": "8c9c1e34-1b75-4e6c-9a77-3d7db7a94f98",
  "text": "The sequence 2, 4, 8, 16 doubles each step."
}
```

### `POST /response`
Submit a user response for scoring or logging.

```json
{
  "id": "8c9c1e34-1b75-4e6c-9a77-3d7db7a94f98",
  "answer": true
}
```

Response (example):

```json
{
  "id": "8c9c1e34-1b75-4e6c-9a77-3d7db7a94f98",
  "correct": true,
  "score_delta": 1
}
```

### `GET /summary`
Optional endpoint to retrieve a running summary.

```json
{
  "items_answered": 10,
  "items_remaining": 90,
  "raw_score": 8
}
```

## Notes

- All items must follow the single-sentence, ESL-friendly rules in the README and `AGENTS.md`.
- Responses should be timestamped and associated with anonymized user/session identifiers for later psychometric analysis.
- Keep payloads compact to support low-latency delivery on constrained devices.
