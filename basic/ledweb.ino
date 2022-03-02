char cmd;

void setup(){
  Serial.begin(9600);
  
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
      
}

void loop(){
  if(Serial.available()){
    cmd = Serial.read();

    if(cmd=='r'){
      digitalWrite(8,HIGH);
      delay(10000);
      digitalWrite(8,LOW);
    }
    else if(cmd=='y'){
      digitalWrite(9,HIGH);
      delay(10000);
      digitalWrite(9,LOW);
    }
    else if(cmd=='g'){
      digitalWrite(10,HIGH);
      delay(10000);
      digitalWrite(10,LOW);
    }
   }
   else{
    Serial.println("error");
    delay(1000);
   }
}
