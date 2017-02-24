int main() {
  string s;
  string t;
  string u;


  s = "hello";
  t = "helll";
  u = "hellp";

  if (eq(s,t)) printd(1); else printd(0);
  if (eq("abc","abc")) printd(1); else printd(0);
  if (eq(t,s)) printd(1); else printd(0);
  if (eq(cat(t,"abc"),cat(u,"ab"))) printd(1); else printd(0);
  if (eq(cat(s,cat(t,u)),cat(s,cat(t,u)))) printd(1); else printd(0);
 
  if (ne(s,t)) printd(1); else printd(0);
  if (ne("abc","abc")) printd(1); else printd(0);
  if (ne(t,s)) printd(1); else printd(0);
  if (ne(cat(t,"abc"),cat(u,"ab"))) printd(1); else printd(0);
  if (ne(cat(s,cat(t,u)),cat(s,cat(t,u)))) printd(1); else printd(0);

  return 0;
}
