using System;
using System.Collections.Generic;
namespace ONP___Transform_the_Expression
{
    class Program
    {
        static void Main(string[] args)
        {
            short n = Convert.ToInt16(Console.ReadLine());
            string[] lines = new string[n];
            string result = "";
            for (int i = 0; i < n; i++)
                lines[i] = Console.In.ReadLine();
            for (int k=0;k<n;k++)
            {
                result = "";
                char[] line = lines[k].ToCharArray();
                Stack<string> operators = new Stack<string>();
                for (int j=0;j<line.Length;j++)
                {
                    switch(line[j])
                    {
                        case '(':
                            break;
                        case '+':
                        case '-':
                        case '/':
                        case '*':
                        case '^':
                            operators.Push(Convert.ToString(line[j]));
                            break;
                        case ')':
                            result = result + operators.Pop();
                            break;
                        default:
                            result = result + Convert.ToString(line[j]);
                            break;
                    }
                }
                Console.WriteLine(result);
            }
        }
    }
}