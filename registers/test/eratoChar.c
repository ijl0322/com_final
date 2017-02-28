
int main() {
 int i,j;
 string tab;
 tab = "0";
 for ( i = 1 ; i < 10 ; i = i+1 )
 tab = tab + "1";
 for ( i = 2 ; i < 100 ; i = i+1 )
 for ( j = i+i; j < 10; j = j+i )
 put_char_at( tab, j, 48 );
 printf(tab);


 return 0;
}