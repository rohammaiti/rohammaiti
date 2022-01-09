/*A rudimentary calculator using switch-case. Truncates operands to integers before using the % operator.*/
#include <stdio.h>
int main(void){
    int operator;
    float left_operand, right_operand;

    while (1)
    {
        printf("Enter left operant:");
        scanf("%f", &left_operand);

        printf("Enter right operand:");
        scanf("%f", &right_operand);

        printf("1. '+' 2. '-' 3. '*' 4. '/' 5. '%%' \n");
        printf("Enter a valid number for operator:");
        scanf("%d", &operator);

        switch (operator)
        {
        case 1: printf("%f\n", left_operand+right_operand);
            break;
        
        case 2: printf("%f\n", left_operand-right_operand);
            break;

        case 3: printf("%f\n", left_operand*right_operand);
            break;

        case 4: printf("%f\n", left_operand/right_operand);
            break;

        case 5: printf("%f\n", (int) left_operand % (int) right_operand);
            break;

        default: printf("Illegal\n");
        }
    }
    return 0;
}












































/*This project is solely made by Roham Maiti. So no cheating please and no plagiarism.*/

