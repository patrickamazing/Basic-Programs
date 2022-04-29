#include <iostream>
using namespace std;

int main()
{
	int a, b; // Tutaj sa zapisane zmienne, ktore beda uzywane w programie.
	cout << "Prosze podac pierwsza liczbe: "; // Tutaj program sie pyta aby wpisac pierwsza zmienna.
	cin >> a; // I ta linia kodu pozwala ja wpisac.
	cout << "Prosze podac druga liczbe: ";
	cin >> b;
	if(a>b) // Jesli a > b, to:
		cout << "Wieksza liczba jest " << a << ", czyli pierwsza liczba ktora podales.";
	else // A jak inaczej, to:
		cout << "Wieksza liczba jest " << b << ", czyli druga liczba ktora podales.";
		
	return(0); // Prosba aby program sie juz zakonczyl, w tym wypdaku z wartoscia 0.		
}

