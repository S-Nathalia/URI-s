#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int n, i, k, leds, size;
  char numb[100];

  scanf("%d", &n);

  for(i = 0; i < n; i++){
    scanf("%s", &numb);
    size = strlen(numb);
    leds = 0;
    for(k = 0; k < size; k ++){
      if(numb[k] == '1') leds += 2;
      if(numb[k] == '2' || numb[k] == '3' || numb[k] == '5') leds += 5;
      if(numb[k] == '4') leds += 4;
      if(numb[k] == '6' || numb[k] == '9' || numb[k] == '0') leds += 6;
      if(numb[k] == '7') leds += 3;
      if(numb[k] == '8') leds += 7;
    }
    printf("%d leds\n", leds);
  }
  return 0;
}
