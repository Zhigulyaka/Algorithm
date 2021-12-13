#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <time.h>

using namespace std;

double textSearch(string ownWord, string searchWord) {
  double timeTrivial;
  clock_t start, end;
  start = clock();
  int* func = new int[ownWord.length()];
  for (int i = searchWord.length(); i < ownWord.length() + searchWord.length(); i++) {
    int s = 0;
    while(searchWord[s] == ownWord[i - (searchWord.length() - s)] && s < searchWord.length()) {
      s++;
    }
    if (s == searchWord.length() &&
        searchWord[searchWord.length() - 1] == ownWord[i - 1])
      func[i - searchWord.length()] = searchWord.length();
    else 
      func[i - searchWord.length()] = 0;
  }
  end = clock();
  timeTrivial = ((double)end - start) / ((double)CLOCKS_PER_SEC);
  return timeTrivial;
}

int* procedureKMP(string searchWord) { 
  int* fn = new int[searchWord.length()];
  int i = 0, j = 0;
  fn[0] = 0;
  while (i < searchWord.length() - 1) {
    j = fn[i];
    while(searchWord[j] != searchWord[j+1] && j>0) {
      j = fn[j-1];
    }
    if (searchWord[j] == searchWord[i+1]) {
      fn[i + 1] = j + 1;
    } else {
      fn[i + 1] = 0;
    }
    i++;
  }
  return fn;
}

double KMP(string ownWord, string searchWord) { 
  double timeKMP;
  clock_t start, end;
  start = clock();
  int* fn = procedureKMP(searchWord);
  int* func = new int[ownWord.length()];
  int i = 0, j = 0;
   if (searchWord[i] == ownWord[i]) 
    func[i] = 1;
  else
    func[i] = 0;
  while (i < ownWord.length() - 1 && j != searchWord.length()) {
    j = func[i];
    if (j == searchWord.length()) 
      j = 0;
    while (searchWord[j] != ownWord[i + 1] && j > 0) 
      j = fn[j - 1];
    if (searchWord[j] == ownWord[i + 1])
      func[i + 1] = j + 1;
    else
      func[i + 1] = 0;
    i++;
  }
  end = clock();
  timeKMP = ((double)end - start) / ((double)CLOCKS_PER_SEC);
  return timeKMP;
}

string inputAlphabet(string ownWord, int length) {
  int countAlph = ownWord.length();
  string alphabet = ownWord;
  ownWord = "";
  for (int i = 0; i < length; i++)
    ownWord += alphabet[rand() % countAlph];
  return ownWord;
}

string generateBigString(string search, int k) {
  string str = "";
  for (int i = 0; i < k; i++) 
      str += search;
  return str;
}

void main(int argc, char *argv[]) { 
  string ownWord = argv[2], searchWord = argv[3];
  int test = atoi(argv[1]), number = atoi(argv[4]);
  string letters;
  int countOwn, countSearch;
  /* string ownWord = "ab", searchWord = "ab";
 int test = 1, number = 100;*/
  double timeTrivial, timeKMP;
  switch (test) {
    case 1:
      ownWord = generateBigString(ownWord, number * 1000);
      searchWord = generateBigString(searchWord, number);
      break;
    case 2:
      ownWord = inputAlphabet(ownWord, 1000001);
      searchWord = generateBigString(searchWord, number);
      break;
    case 3:
      ownWord = generateBigString(ownWord, number);
      break;
    case 4:
      letters = argv[2];
      countOwn = atoi(argv[3]);
      countSearch = atoi(argv[4]);
      ownWord = inputAlphabet(letters, countOwn);
      searchWord = inputAlphabet(letters, countSearch);
      break;
    case 5:
      countOwn = atoi(argv[4]);
      countSearch = atoi(argv[5]);
      ownWord = generateBigString(ownWord, countOwn);
      searchWord = generateBigString(searchWord, countSearch);
      break;
    default:
      break;
  }
  timeTrivial = textSearch(ownWord, searchWord);
  timeKMP = KMP(ownWord, searchWord);
  cout << timeTrivial << " " << timeKMP;
}

