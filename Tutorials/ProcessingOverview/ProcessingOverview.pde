import java.util.Arrays;

int[][] savedLines = {};

void setup() {
    size(620, 480, P2D);
    stroke(255);
}

void draw() {
    background(192, 64, 0);

    for (int[] line : savedLines) {
        // Draw saved lines
        line(width/2, height/2, line[0], line[1]);
    }

    line(width/2, height/2, mouseX, mouseY);
}

int[][] appendToArray(int[][] originalArr, int[] toAppend) {
    int[][] tempArray = Arrays.copyOf(originalArr, originalArr.length + 1);
    tempArray[tempArray.length - 1] = toAppend;

    return tempArray;
}

void mousePressed() {
    savedLines = appendToArray(savedLines, new int[] {mouseX, mouseY});;
}
