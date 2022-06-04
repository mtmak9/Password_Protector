Developer:
---------------------
|    MTMAK9   |
---------------------

"Password Protector"

Program do szyfrowania pliku tekstowego i całej zawartości.
Aplikacja wykorzystuje szyfrowanie z biblioteki kryptograficznej.
Dzięki temu programowi możesz zaszyfrować każdą informacje w pliku tekstowym który można odszyfrować tylko przez tę aplikacje,
jest to doskonałe rozwiązanie dla delikatnych informacji takich jak hasła,loginy lub wrażliwe dane którychy nie chcielibyśmy aby trafiły w nie powołane
ręce. Aplikacja jest prosta i posiada podstawowe funkcje ułożone w taki sposób aby program nie zablokował dostępu.
Jeśli program z jakiegoś powodu straci dostęp do plików szyfrowania lub hasła, posiadam programy dekodujące pliki, które odszyfrują zawartość, jeśli program stracił do nich dostęp.

Hasło domyślne: 0000

Tłumaczenie poszczególnych opcji:

1.Open File - otwiera zaszyfrowany plik odszyfrowując go i otwierając, przy zamknięciu pliku dokonywana jest ponownie Enkrypcja pliku. (enc_file.txt -> file.txt -> enc_file.txt)
2.Close File - Wymusza zamknięcie i zaszyfrowanie pliku jeśli z jakiegoś powodu nie udało się tego zrobić, lub zaistniał błąd w aplikacji. (file.txt -> enc_file.txt)
3.Password - Możliwość zmiany hasła dostępu do aplikacji na inne
	1.Encrypt Password - Zakodowanie hasła jeśli zostało odkodowane w pliku (key.txt -> enc_key.txt)
	2.Decrypt Password - Odkodowanie hasła jeśli zostało/jest zakodowane w pliku (enc_key.txt -> key.txt)
	3.Change Password - Zmiana hasła na inne: (enc_key.txt -> key.txt -> Możliwość edycji pliku i zapisanie nowego hasła w notatniku)
	4.Back - Powrót do poprzedniego Menu i zaszyfrowanie pliku z hasłem (key.txt -> enc_key.txt -> exit)
4.Encryption
	1.Encryption File - Zakodowanie Głównego pliku w razie problemów(opcjonalnie)
	2.Decryption File - Odkodowanie głównego pliku w razie problemów(opcjonalnie)
	3.Back - powrót do poprzednich opcji

Obsługa programu:

Program jest bardzo prosty w obsłudze, gdy uruchomisz aplikacje aby uzyskać dostęp do niej musisz wpisać hasło, jeśli hasło jest prawidłowe to uzyskasz dostęp do wszystkich
funkcji aplikacji, jeśli hasło jest nieprawidłowe to po 3 próbach aplikacja zostanie zamknięta.

Po wpisaniu poprawnego hasła, możemy otworzyć nasz zaszyfrowany plik opcją nr: 1.
Edytujemy plik wg. własnej woli i zapisujemy go funkcją w notatniku i zamykamy notatnik. Plik zostanie automatycznie zaszyfrowany po zamknięciu go.
Następnie możemy wyjść z aplikacji wybierając opcje 5, program ponownie sprawdzi czy plik wymaga szyfrowania i aplikacja zostanie zamknięta.

UWAGA!
Nie usuwaj żadnych plików tekstowych z folderu, ponieważ są one potrzebne do prawidłowego funkcjonowania aplikacji, jeśli któryś z plików zostanie usunięty, program 
straci dostęp do głównego pliku i cała zawartość może przepaść.

W pliku "enc_file.txt" jest zapisana cała zawartość ukryta w aplikacji, jeśli ten plik przepadnie to zawartość jest nie do odzyskana, jeśli stracisz któryś z innych plików,
możesz się ze mną skontaktować w celu uzyskania programów dekodujących plik dzięki którym jest możliwe odzyskanie zawartości zakodowanego pliku.
