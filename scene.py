from manim import *


class ExampleAtoms(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2.2, 0.2],
            y_range=[0, 5, 1],
            x_length=10,
            axis_config={"color": WHITE},
        )

        axes_labels = axes.get_axis_labels(x_label="t", y_label=Tex("T($ C^\circ $)"))

        vg = VGroup()

        vg.add(axes, axes_labels)

        for i in range(20):
            x = i * 0.1
            fx = 0.5 * np.sin(2 * PI * x) + 2 * x
            dot = Dot(axes.coords_to_point(x, fx), color=BLUE)
            # dot.add_updater(lambda obj: obj.move_to(axes.coords_to_point(x, fx)))
            vg.add(dot)

        self.play(Write(vg), run_time=3)
        self.wait(3)
        self.play(vg.animate.scale(0.4).move_to(3 * LEFT))
        self.wait(2)
