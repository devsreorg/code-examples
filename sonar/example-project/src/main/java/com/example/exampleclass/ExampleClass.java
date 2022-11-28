package com.example.exampleclass;

public class ExampleClass {
    public static void main(String[] args) {
        System.out.println(sumOfPrimes(10));
        System.out.println(getWords(10));
    }

    static int sumOfPrimes(int max) {
        int total = 0;
        OUT: for (int i = 1; i <= max; ++i) {
            for (int j = 2; j < i; ++j) {
                if (i % j == 0) {
                    continue OUT;
                }
            }
            total += i;
        }
        return total;
    }

    static String getWords(int number) {
        switch (number) {
            case 1:
                return "one";
            case 2:
                return "a couple";
            case 3:
                return "a few";
            default:
                return "lots";
        }
    }
}
