from manim import *


class ExampleAtoms(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2.1, 0.2],
            y_range=[0, 5, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
        )

        axes_labels = axes.get_axis_labels(x_label="t", y_label=Tex("T($ C^\circ $)"))

        vg = VGroup()

        vg.add(axes, axes_labels)
        npoints = 50
        for i in range(npoints):
            dx = 2 / npoints
            x = i * dx
            fx = 0.5 * np.sin(2 * PI * x) + 2 * x
            dot = Dot(
                axes.coords_to_point(x, fx), color=BLUE, radius=DEFAULT_SMALL_DOT_RADIUS
            )
            # dot.add_updater(lambda obj: obj.move_to(axes.coords_to_point(x, fx)))
            vg.add(dot)

        self.play(Write(vg), run_time=4)
        self.wait(1)
        self.play(vg.animate.scale(0.5))
        self.wait()
        self.play(vg.animate.shift(4 * LEFT).scale_to_fit_width(0.7 * vg.width))
        self.wait(2)
