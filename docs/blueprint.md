# SmartLibrary — Project Blueprint

## Stack
- **Backend:** Python, FastAPI, SQLAlchemy (async), SQLite
- **Frontend:** Streamlit
- **Auth:** JWT tokens, bcrypt passwords
- **Database:** SQLite via aiosqlite async driver

## User Tiers
- **Guest** — browse and search only, no login required
- **Member** — reserve, checkout, waitlist, recommendations
- **Librarian/Admin** — inventory management, overrides, all checkouts view

## Project Structure
```
smartlibrary/                          # git root
├── .env                               # secrets — never commit
├── .env.example                       # committed template
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── books.csv
├── backend/
│   └── app/
│       ├── main.py
│       ├── config.py                  # ✅ done
│       ├── auth/
│       │   ├── jwt_handler.py
│       │   ├── dependencies.py
│       │   ├── password.py
│       │   └── router.py
│       ├── models/
│       │   ├── base.py                # ← start here
│       │   ├── user.py
│       │   ├── book.py
│       │   ├── cart.py
│       │   ├── checkout.py
│       │   └── waitlist.py
│       ├── schemas/
│       │   ├── auth.py
│       │   ├── user.py
│       │   ├── book.py
│       │   ├── cart.py
│       │   ├── checkout.py
│       │   ├── waitlist.py
│       │   └── search.py
│       ├── repositories/
│       │   ├── base_repo.py
│       │   ├── user_repo.py
│       │   ├── book_repo.py
│       │   ├── cart_repo.py
│       │   ├── checkout_repo.py
│       │   └── waitlist_repo.py
│       ├── services/
│       │   ├── auth_service.py
│       │   ├── search_service.py
│       │   ├── cart_service.py
│       │   ├── checkout_service.py
│       │   ├── waitlist_service.py
│       │   └── recommendation.py
│       ├── routers/
│       │   ├── auth.py
│       │   ├── books.py
│       │   ├── users.py
│       │   ├── cart.py
│       │   ├── checkout.py
│       │   ├── waitlist.py
│       │   └── recommendations.py
│       └── db/
│           ├── session.py             # ✅ done
│           └── seed.py
├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── 1_login.py
│   │   ├── 2_register.py
│   │   ├── 3_dashboard.py
│   │   ├── 4_browse.py
│   │   ├── 5_my_books.py
│   │   ├── 6_waitlist.py
│   │   └── 7_admin.py
│   └── utils/
│       ├── api_client.py
│       └── session.py
└── tests/
    ├── conftest.py
    ├── test_auth.py
    ├── test_search.py
    ├── test_cart.py
    ├── test_checkout.py
    └── test_waitlist.py
```

## Key Design Decisions
- Routers are thin — call services only, 5-10 lines max
- Services have pure business logic — no HTTP, no DB calls
- Repositories handle all DB queries — no logic
- Enums for all categorical values
- Relative imports throughout backend (`from ..config import settings`)
- Always run app from project root (`smartlibrary/`)
- `.env` at project root, loaded via pydantic-settings

## Features
- Book search by ISBN, title, author, genre, age group, lexile level, publisher, tags
- Cart system with TTL expiry (CART_TTL_MINUTES in .env)
- Checkout with age-gate restrictions
- Waitlist queue for unavailable books with notification window
- Recommendation engine using heapq scoring
- Concurrency safe — row-level locking, async sessions, one session per request

## Build Order
- [x] Step 1 — venv, folder structure, requirements.txt, .env
- [x] Step 2 — config.py + db/session.py
- [ ] Step 3 — models/ (start here — base.py first)
- [ ] Step 4 — db/seed.py
- [ ] Step 5 — auth/ (register, login, JWT)
- [ ] Step 6 — repositories/
- [ ] Step 7 — services/search_service.py
- [ ] Step 8 — services/cart_service.py
- [ ] Step 9 — services/checkout_service.py
- [ ] Step 10 — services/waitlist_service.py
- [ ] Step 11 — services/recommendation.py
- [ ] Step 12 — routers/
- [ ] Step 13 — frontend/
- [ ] Step 14 — tests/

## Environment
- OS: Windows 10, Git Bash terminal in VSCode
- Python: 3.12.10 in venv at smartlibrary/venv/
- GitHub: https://github.com/devcommando/smart-library
- Always activate venv: `source venv/Scripts/activate`
- Always run from project root: `smartlibrary/`