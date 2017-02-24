
/* Eratosthene */

#define N 100
#define SN 10		/* sqrt(n) */

string tab;

int main() {
  int i,j;
  tab = "0";
  for ( i = 1 ; i < N ; i = i+1 )
    tab = tab + '1';
  for ( i = 2 ; i < SN ; i = i+1 )
    for ( j = i+i; j < N ; j = j+i ) 
      put_char_at( tab, j, '0' );
  
  for ( i = 0 ; i < N ; i = i+1 )
    if ( get_char_at( tab, i ) == '1' ) {
      printd(i);
      printf(" ");
    }
  printf("\n");
  return 0;
}


