package tableroseljava;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class TableroSeljava extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Crear un panel principal con un borde y un layout VBox
        VBox mainPanel = new VBox();
        mainPanel.setPadding(new Insets(20));

        // Crear un panel para los botones con HBox horizontal
        HBox buttonPanel = new HBox();
        buttonPanel.setSpacing(20);

        // Crear y añadir los botones al panel de botones
        Button yesButton = new Button("Yes");
        Button noButton = new Button("No");
        Button cancelButton = new Button("Cancel");

        // Agregar un método de acción a cada botón
        yesButton.setOnAction(event -> {
            System.out.println("Yes button was clicked!");
        });

        noButton.setOnAction(event -> {
            System.out.println("No button was clicked!");
        });

        cancelButton.setOnAction(event -> {
            System.out.println("Cancel button was clicked!");
        });

        buttonPanel.getChildren().addAll(yesButton, noButton, cancelButton);

        // Añadir el panel de botones al centro del panel principal
        mainPanel.getChildren().add(buttonPanel);

        // Crear una escena y añadir el panel principal
        Scene scene = new Scene(mainPanel, 200, 100);

        // Crear un Stage y añadir la escena
        primaryStage.setScene(scene);
        primaryStage.setTitle("Layouts");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}


