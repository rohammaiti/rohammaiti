#include <iostream>
#include <cmath>

using namespace std;

class Calculator 
{
public:
    double addNumber(const double numbers[], int n) 
    {
        double sum = 0.0;
        for (int i = 0; i < n; ++i) 
        {
            sum += numbers[i];
        }
        return sum;
    }

    double multiplyNumber(const double numbers[], int n) 
    {
        double product = 1.0;
        for (int i = 0; i < n; ++i) 
        {
            product *= numbers[i];
        }
        return product;
    }

    double subtract(double a, double b) 
    {
        return a - b;
    }

    double divide(double Dividend, double Divisor) 
    {
        return Dividend / Divisor;
    }
};

class SciCalculator : public Calculator 
{
public:
    double Percentage(double value, double percentage) 
    {
        return (value * percentage) / 100.0;
    }

    int Factorial(int n) 
    {
        if (n == 0 || n == 1) 
        {
            return 1;
        } 
        else 
        {
            return n * Factorial(n - 1);
        }
    }

    double Square(double num) 
    {
        return num * num;
    }

    double SquareRoot(double num) 
    {
        return sqrt(num);
    }
};

int main() 
{
    SciCalculator sciCalculator;

    int choice;

    do {
        cout << "Select operation: \n"
             << "1. Addition\n"
             << "2. Subtraction\n"
             << "3. Multiplication\n"
             << "4. Division\n"
             << "5. Percentage\n"
             << "6. Factorial\n"
             << "7. Square\n"
             << "8. Square Root\n"
             << "0. Exit\n"
             << "Enter choice (0-8): ";
        cin >> choice;

        if (choice == 0) 
        {
            cout << "Exiting..." << endl;
            break; 
        }

        if (choice >= 1 && choice <= 4) 
        {
            int size;
            cout << "Enter the number of elements- ";
            cin >> size;

            double *numbers = new double[size];

            cout << "Enter the elements-" << endl;
            for (int i = 0; i < size; ++i) 
            {
                cin >> numbers[i];
            }

            if (choice == 1) 
            {
                double result = sciCalculator.addNumber(numbers, size);
                cout << "Sum: " << result << endl;
            }

            else if (choice == 2) 
            {
                double result = sciCalculator.subtract(numbers[0], numbers[1]);
                cout << "Difference: " << result << endl;
            }

            else if (choice == 3) 
            {
                double result = sciCalculator.multiplyNumber(numbers, size);
                cout << "Product: " << result << endl;
            } 
            
            else if (choice == 4) 
            {
                if (numbers[1] != 0) 
                {
                    double result = sciCalculator.divide(numbers[0], numbers[1]);
                    cout << "Quotient: " << result << endl;
                } 
                else 
                {
                    cout << "Error: Division by zero" << endl;
                }
            }

            delete[] numbers;

        } 
        else if (choice >= 5 && choice <= 8) 
        {
            double num;
            cout << "Enter a number: ";
            cin >> num;

            if (choice == 5) 
            {
                double percentage;
                cout << "Enter the percentage: ";
                cin >> percentage;
                double result = sciCalculator.Percentage(num, percentage);
                cout << "Percentage: " << result << endl;
            } 
            
            else if (choice == 6) 
            {
                int result = sciCalculator.Factorial(static_cast<int>(num));
                cout << "Factorial: " << result << endl;
            } 
            
            else if (choice == 7) 
            {
                double result = sciCalculator.Square(num);
                cout << "Square: " << result << endl;
            } 
            
            else if (choice == 8) 
            {
                if (num >= 0) 
                {
                    double result = sciCalculator.SquareRoot(num);
                    cout << "Square Root: " << result << endl;
                } 
                else 
                {
                    cout << "Error: Cannot calculate square root of a negative number." << endl;
                }
            }
        } 
        
        else 
        {
            cout << "Invalid choice. Please select 0 to 8." << endl;
        }
    } 
    while (choice != 0);
    return 0;
}