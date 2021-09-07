from vispy import app, gloo
from vispy.gloo import Program
import numpy as np

vertex = """
    uniform float theta;
    uniform mat4 model;
    uniform vec4 color;
    attribute vec2 position;
    varying vec4 v_color;
    void main()
    {
        float x = 0.25 * position.x;
        float y = 0.25 * position.y;
        gl_Position = model * vec4(x, y, 0.0, 1.0);
        v_color = vec4(position.x,position.y,0.5,1);
    } """

fragment = """
    varying vec4 v_color;
    void main()
    {
        gl_FragColor = v_color;
    } """


class AppCanvas(app.Canvas):
    def __init__(self):
        super().__init__(size=(512, 512))
        self.program = Program(vertex, fragment, count=4)
        self.program['color'] = (1,0,0,1)
        self.program['position'] = np.array([[-1,-1],[-1,1],[1,-1],[1,1]], dtype=np.float32)

        self.program['theta'] = 0.0
        modelMatrix = np.eye(4, dtype=np.float32)
        self.program['model'] = modelMatrix
        gloo.set_viewport(0, 0, *self.physical_size)
        gloo.set_clear_color('white')

    def on_draw(self, event):
        gloo.clear()
        self.program.draw('triangle_strip')
    
    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.physical_size)