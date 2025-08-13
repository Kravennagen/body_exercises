from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QWidget, QVBoxLayout
from PyQt6.QtSvgWidgets import QGraphicsSvgItem
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QMouseEvent


class BodyViewer(QWidget):
    def __init__(self, gender):
        super().__init__()
        self.setWindowTitle(f"{gender.capitalize()} Body Viewer")
        self.gender = gender
        self.selected_muscles = set()

        layout = QVBoxLayout()
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()

        svg_path = f"assets/{gender}_body.svg"
        self.svg_item = QGraphicsSvgItem(svg_path)
        self.svg_item.setFlags(QGraphicsSvgItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(self.svg_item)

        self.view.setScene(self.scene)
        layout.addWidget(self.view)
        self.setLayout(layout)

        # Click handling via mouse event filter
        self.view.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == event.Type.MouseButtonPress and isinstance(event, QMouseEvent):
            pos = self.view.mapToScene(event.position().toPoint())
            item = self.scene.itemAt(pos, self.view.transform())
            if item == self.svg_item:
                print("Clicked on base SVG")
            else:
                if item:
                    muscle_id = item.data(0)  # Store muscle name in item data
                    if muscle_id:
                        print(f"Muscle clicked: {muscle_id}")
                        self.selected_muscles.add(muscle_id)
            return True
        return super().eventFilter(obj, event)
