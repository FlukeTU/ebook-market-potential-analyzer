# E-Book Market Potential Analyzer

A machine learning-based decision-support application for evaluating the market potential of e-books on online platforms.

This project combines data science, machine learning, backend API deployment, and web application design to transform a trained model into an interactive prototype that can be used for business decision support.

---

## Project Overview

The **E-Book Market Potential Analyzer** estimates whether an e-book has strong commercial potential based on observable market signals such as rating, reviews, price, book age, category, seller type, and Kindle Unlimited status.

The goal of this project is not only to build a predictive model, but also to convert the model into a usable application that can help users compare different business scenarios.

For example, users can explore questions such as:

- What happens if the book price is reduced?
- Does Kindle Unlimited status improve the estimated market potential?
- How does the number of reviews affect the predicted result?
- Which type of book profile appears more commercially promising?

---

## Project Objective

The objective of this project is to develop a machine learning-based decision-support system for evaluating the market potential of e-books.

Specifically, the project aims to:

1. Analyze key factors associated with e-book market success.
2. Build and compare machine learning models for bestseller classification.
3. Handle class imbalance in the target variable.
4. Select a final model that balances performance, interpretability, and practical usefulness.
5. Deploy the trained model as a backend API.
6. Build a user-friendly web interface for scenario-based decision support.

---

## Dataset

This project uses the **Amazon Kindle Books Dataset 2023**, which contains product-level information about e-books listed on an online platform.

The dataset includes variables such as:

- Book title
- Author
- Seller
- Star rating
- Number of reviews
- Price
- Kindle Unlimited status
- Book category
- Published date
- Bestseller status

The target variable used in this project is:

```text
isBestSeller