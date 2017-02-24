

int main() {
  string tab;
  int i,j;
  tab = "0";
  for ( i = 1 ; i < 100 ; i = i+1 )
    tab = tab + '1';
  for ( i = 2 ; i < 10 ; i = i+1 )
    for ( j = i+i; j < 100; j = j+i ) 
      put_char_at( tab, j, '0' );
  
  for ( i = 0 ; i < 100 ; i = i+1 )
    if ( get_char_at( tab, i ) == '1' ) {
      printd(i);
      printf(" ");
    }
  printf("\n");
  return 0;
}


