int g = 9;
int r = 10;
int b = 11;
int y = 3;
int w = 5;

int rr = 40;
int rg = 30;
int ry = 30;
int rw = 8;
int rb = 8;

void setup() {
    Serial.begin(9600);
    pinMode(r, OUTPUT);
      pinMode(g, OUTPUT);
     pinMode(b, OUTPUT);
       pinMode(y, OUTPUT);
  pinMode(w, OUTPUT);

}


void loop() {
  if(Serial.available() > 0) {
    
   int data = Serial.read();
    Serial.print(data);
    data = data-48;
    if(data == 1){
      shine(g, 250);
      shine(r, random(rr)/1);
      shine(b, random(rb)/1);
      shine(y, random(ry)/1);
      shine(w, random(rw)/1);
    }
    else if (data == 2){
      shine(r,250);
      shine(g,random(rg)/1);
      shine(b,random(rb)/1);
      shine(y,random(ry)/1);
      shine(w,random(rw)/1);
    }
    else if (data == 3){
      shine(y,250);
      shine(r,random(rr)/1);
      shine(g,random(rg)/1);
      shine(b,random(rb)/1);
      shine(w,random(rw)/1);
    }
    else if (data == 4){
      shine(b,200);
      shine(r,random(rr)/1);
      shine(g,random(rg)/1);
      shine(y,random(ry)/1);
      shine(w,random(rw)/1);
    }
    else if (data == 5){
      shine(w,30);
      shine(r,random(rr)/1);
      shine(g,random(rg)/1);
      shine(b,random(rb)/1);
      shine(y,random(ry)/1);
    }
    
}
}

void shine(int pinNum, int intensity){
  analogWrite(pinNum, intensity); 
}





      
  

  
