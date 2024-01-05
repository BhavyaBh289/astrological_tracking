  
const int inputPinX = 4;
const int outputPinX = 3;
const int countThresholdX = 10;

int countX = 0;
int prevInputStateX = LOW;
bool alreadyCountedX = false;

void setup() {
  pinMode(inputPinX, INPUT);
  pinMode(outputPinX, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // Check X count
  int inputStateX = digitalRead(inputPinX);

  if (inputStateX == HIGH && prevInputStateX == LOW && !alreadyCountedX) {
    countX++;
    Serial.print("Count X: ");
    Serial.println(countX);

    if (countX >= countThresholdX) {
      Serial.println("Count threshold X reached. Changing output pin X state.");
      digitalWrite(outputPinX, HIGH);
      countX = 0;
    }

    alreadyCountedX = true;
  } else if (inputStateX == LOW) {
    alreadyCountedX = false;
  }

  prevInputStateX = inputStateX;

  delay(100);
}
