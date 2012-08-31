#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) {
  char * loc;
  char * barf = "Content-Type: text/plain;charset=us-ascii\n\nBARF!!!\n\n";
  
  char * sn = getenv("SERVERNAME");
  char * req = getenv("REQUEST_URI");
  char * r = "/tiles/tnm";
  
  if (sn == NULL || req == NULL) {
    printf(barf);
    return(0);
  }
   
  int n = strlen(req);
  int ext = 0;
  int ys = 0;
  int xs = 0;
  int zs = 0;
  
  while (n-- >= 0) {
    if ('.' == req[n])
      ext = n;
      
    if ('/' == req[n]) 
      if (ys == 0) 
        ys = n;
      else if (xs == 0)
        xs = n;
      else if (zs == 0) {
        zs = n;   
        break;
      }
    }
  }
  
  if (ext == 0) ext = strlen(req);

  // Hope 16 chars is enough... guess I could use malloc...
  char * y = malloc(ext - ys + 1);
  char * x = malloc(ys - xs + 1);
  char * z = malloc(xs - zs + 1);

  y = strcpy(req + ys, ext - ys);
  x = strcpy(req + xs, ys - xs);
  z = strcpy(req + zs, xs - zs);
  
  if (atoi(z) < 16) {
    loc = malloc(512);
    loc = sprintf("http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile/%s/%s/%s.png", z, y, x)
    
  } else {
  }
  
  printf("Location:     %s\r\n\r", loc);
  return(0);
}