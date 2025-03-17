// massiv.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    setlocale(LC_ALL, "RU");

    int  z2 = 0, pr = 1, t, k = 0;
    const int N = 10;
    float mas[N];
    float arr1[N];
    float arr2[N];
    float max;
    int r = 0, j = 0;

    int z1 = 0;


    for (int i = 0; i < N; i++)
    {
        cout << "Введите число " << i << " :";
        cin >> mas[i];
    }

    max = mas[0];

    for (int i = 0; i < N; i++)
    {
        if (mas[i] > max)
        {
            max = mas[i];
            k = i;
        }

    }
    cout << "Максимальное число  : " << max << endl << "Индекс  :" << k << endl;;


    for (int i = 0; i < N; i++)
    {
        if (mas[i] == 0)
        {
            z1 = i;
            break;

        }
        else if (i < N)
        {
            continue;
        }
        else
        {
            cout << "Нолей в массиве нет" << endl;
            break;
        }

    }

    for (int i = z1 + 1; i < N; i++)
    {
        if (mas[i] == 0)
        {
            z2 = i;
            break;

        }
        else if (i < N)
        {
            continue;
        }

        else
        {
            cout << "Нет второго нуля" << endl;
            break;
        }

    }


    for (int i = z1 + 1; i < z2; i++)
    {
        t = mas[i];
        pr *= t;

    }
    cout << "Произведение элементов  : " << pr << endl;

    for (int i = 0; i < N; i++)
    {
        if (i % 2 != 0)
        {
            arr1[r] = mas[i];
            r++;
        }
        else
        {
            arr2[j] = mas[i];
            j++;
        }
    }

    for (int i = 0; i < r; i++)
    {
        mas[i] = arr1[i];
    }
    for (int i = r, u = 0; i < N; i++, u++)
    {
        mas[i] = arr2[u];
    }


    cout << "Измененный массив :";
    for (int i = 0; i < N; i++)
    {
        cout << mas[i] << " ";
    }
    cout << endl;
}