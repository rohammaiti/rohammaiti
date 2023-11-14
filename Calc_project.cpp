#include <iostream>
#include <cmath>

using namespace std;

class Calculator 
{
    public:
        double addNumber(const double numbers[], int n) {
            double sum = 0.0;
            for (int i = 0; i < n; ++i) {
                sum += numbers[i];
            }
            return sum;
        }

        double multiplynumber(const double numbers[], int n) {
            double product = 1.0;
            for (int i = 0; i < n; ++i) {
                product *= numbers[i];
            }
            return product;
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

        double calculatePower(double x, double y) 
        {
            return pow(x, y);
        }

        double subtract(double a, double b) 
        {
            return a - b;
        }

        double divide(double dividend, double divisor) 
        {
            if (divisor != 0) 
            {
                return dividend / divisor;
            } 
            
            else 
            {
                cout << "Error: Division by zero is undefined." << endl;
                return NAN;
            }
        }
};

int main() 
{
    SciCalculator sciCalculator;
    int choice;

    do 
    {
        cout << "Select operation: \n"
             << "1. Addition\n"
             << "2. Multiplication\n"
             << "3. Subtraction\n"
             << "4. Division\n"
             << "5. Percentage\n"
             << "6. Factorial\n"
             << "7. Square\n"
             << "8. Square Root\n"
             << "9. Power\n"
             << "0. Exit\n"
             << "Enter choice (0-9): ";
        cin >> choice;

        if (choice == 0) 
        {
            cout << "Exiting..." << endl;
            break;
        }

        if (choice == 1 || choice == 2) 
        {
            int size;
            cout << "Enter the number of elements: ";
            cin >> size;

            double *numbers = new double[size];

            cout << "Enter the elements, separated by spaces:" << endl;
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
                double result = sciCalculator.multiplynumber(numbers, size);
                cout << "Product: " << result << endl;
            }

            delete[] numbers;
        } 
        
        else if (choice == 3 || choice == 4) 
        {
            double num1, num2;
            cout << "Enter the first number: ";
            cin >> num1;
            cout << "Enter the second number: ";
            cin >> num2;

            if (choice == 3) 
            {
                double result = sciCalculator.subtract(num1, num2);
                cout << "Difference: " << result << endl;
            } 
            
            else if (choice == 4) 
            {
                if (num2 != 0) 
                {
                    double result = sciCalculator.divide(num1, num2);
                    cout << "Quotient: " << result << endl;
                } 
                
                else {
                    cout << "Error: Division by zero is undefined." << endl;
                }
            }
        } 
        
        else if (choice >= 5 && choice <= 9) 
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
            
            else if (choice == 9) 
            {
                double exponent;
                cout << "Enter the exponent for power calculation: ";
                cin >> exponent;
                double result = sciCalculator.calculatePower(num, exponent);
                cout << num << " ^ " << exponent << " = " << result << endl;
            }
        } 
        
        else 
        {
            cout << "Invalid choice. Please select 0 to 9." << endl;
        }

    } while (choice != 0);

    return 0;
}
