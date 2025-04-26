// import java.io.File;
// import java.io.FileNotFoundException;
// import java.io.FileWriter;
// import java.io.IOException;
// import java.util.Scanner;

// public class ReadFile {

// 	public static void main(String[] args) throws IOException {

// 		File file = new File("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/demo.txt");
// 		Scanner scan = new Scanner(file);

// 		String fileContent = "THIS IS A NEW FILE MADE BY US\n";
// 		while (scan.hasNextLine()) {
// 			fileContent = fileContent.concat(scan.nextLine() + "\n");
// 		}

// 		FileWriter writer = new FileWriter("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/newfile.txt");
// 		writer.write(fileContent);
// 		writer.close();

// 	}

// }

//link to source code: https://github.com/alexlorenlee/JavaTutorialCode/blob/master/Programs/ReadFile.java