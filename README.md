## Purchase Approval

Custom app for purchase approval workflow

#### License

mit

# Purchase Approval App

## Overview
This custom Frappe app implements a Purchase Approval Request workflow
to control high-value purchase requests.

## Features
- Custom DocType: Purchase Approval Request
- Automatic priority handling based on amount and item count
- Role-based approval (Purchase Manager)
- Server-side validation and permission enforcement
- SQL Query Report: Approved High-Value Purchases
- Dummy data auto-created on app installation

## Installation
```bash
bench get-app purchase_approval <repository_url>
bench --site yoursite.local install-app purchase_approval
