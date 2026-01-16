# MongoDB Migration Tool (Python)

A simple, configuration-driven Python utility to safely add new fields to existing MongoDB documents using an asynchronous approach.

---

## What problem does this solve?

In real applications, database requirements change over time.  
New fields often need to be added to existing MongoDB documents without deleting or breaking old data.

This tool demonstrates how to perform such updates safely using Python.

---

## What is MongoDB Migration?

MongoDB migration means updating existing documents when the database structure changes.

### Example

#### Before Migration
```json
{
  "_id": 1,
  "name": "Virat"
}
```

#### After Migration
```json
{
  "_id": 1,
  "name": "Virat",
  "country": "India"
}
```

---

## Features

- **Idempotent**  
  Only updates documents where the target field does not exist.  
  Running the script multiple times is safe.

- **Asynchronous**  
  Built using Motor for non-blocking and high-performance MongoDB operations.

- **Configuration-driven**  
  Database name, collection name, field name, and value are controlled using environment variables.

- **Safe Migration**  
  Existing data is never deleted or overwritten.

---

## Project Structure

```
mongodb-migration/
│
├── migrate.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/sowmya-rapid/mongodb-migration.git
cd mongodb-migration
```

---

### 2. Create environment file
```bash
cp .env.example .env
```

---

### 3. Configure environment variables

Edit the `.env` file:

```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=migration_demo
COLLECTION_NAME=users
FIELD_NAME=created_at
FIELD_VALUE=auto
```

---

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 5. Run the migration
```bash
python migrate.py
```

---

## How it Works

1. Connects to MongoDB using the provided URI.
2. Scans the specified collection.
3. Finds documents where the target field does not exist.
4. Adds the new field using the `$set` operator.
5. Leaves all existing data untouched.

---

## Why is this safe?

- No documents are deleted.
- No existing fields are modified.
- Only missing fields are added.
- Script can be run multiple times without side effects.

---

## When should this tool be used?

- Adding new fields to existing MongoDB collections
- Handling schema changes safely
- Performing background database upgrades
- Production-safe MongoDB migrations

---

## Conclusion

This project demonstrates a clean, safe, and scalable approach to MongoDB migration using Python and asynchronous database operations.

