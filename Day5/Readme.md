# Metrics Calculation

## Confusion Matrix

                 Predicted
                0       1
    Actual  0  TN      FP
            1  FN      TP

## Formulas

-   Accuracy\
    (TP + TN) / (TP + TN + FP + FN)

-   Precision\
    TP / (TP + FP)

-   Recall\
    TP / (TP + FN)

## Example

    [[3 1]
     [2 4]]

-   TN = 3, FP = 1, FN = 2, TP = 4

Accuracy = (4 + 3) / 10 = 0.7\
Precision = 4 / 5 = 0.8\
Recall = 4 / 6 = 0.67
