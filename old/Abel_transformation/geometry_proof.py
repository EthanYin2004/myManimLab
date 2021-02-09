from manimlib.imports import *

class Abel(Scene):
    CONFIG = {"camera_config": {"background_color": BLACK_BOARD}}
    def construct(self):
        wood_bar = ImageMobject("/Users/ytj/Desktop/wood.jpeg").set_height(0.5,stretch=True).set_width(15,stretch=True).to_edge(DOWN,buff=0)
        self.add(wood_bar)
        rec_group = VGroup()
        for i in range(6):
            for j in range(i+1):
                rec = Square().set_height(0.8)
                rec.shift(DOWN*i*0.8+LEFT*j*0.8)
                rec_group.add(rec)
        rec_group.move_to(ORIGIN)
        rec_group.set_opacity(1)
        rec_group.set_sheen(0.6,DR).set_color([BLUE_A,BLUE_E])
        rec_group.shift(RIGHT*4+UP*0.5)
        text_title = Text("阿贝尔变换(Abel transformation)", font='SetoFont SC').scale(0.8).shift(LEFT*3.5+UP*3.2).set_color(YELLOW)
        sub_title_1 = Text("设想我们手头有两个数列",font='SetoFont SC').shift(DOWN*3)
        tex_1 = TexMobject("\{a_{n}\}",":","a_{1}",",","a_{2}",",","a_{3}","...","a_{n}").scale(0.8).next_to(text_title,DOWN).align_to(text_title,LEFT)
        tex_2 = TexMobject("\{b_{n}\}", ":", "b_{1}", ",", "b_{2}", ",", "b_{3}", "...","b_{n}").scale(0.8).next_to(tex_1,
                                                                                                            DOWN).align_to(
            text_title, LEFT)
        self.add(text_title)
        self.play(FadeInFromPoint(sub_title_1,sub_title_1.get_center()))
        self.play(FadeInFromPoint(tex_1[0],tex_1[0].get_center()))
        self.wait(0.5)
        self.play(FadeInFrom(tex_1[1:],LEFT))
        self.play(FadeInFromPoint(tex_2[0], tex_2[0].get_center()))
        self.wait(0.5)
        self.play(FadeInFrom(tex_2[1:], LEFT))
        self.wait()
        sub_title_2_1 = Text("记",font='SetoFont SC')
        sub_title_2_2 = TexMobject("A_{k}=a_{1}+a_{2}+a_{3}+...+a_{k}").set_color(YELLOW)
        sub_title_2_2.next_to(sub_title_2_1,RIGHT)
        sub_title_2 = VGroup(sub_title_2_1,sub_title_2_2)
        sub_title_2.move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_1))
        self.play(FadeInFromPoint(sub_title_2,sub_title_2.get_center()))
        tex_3 = sub_title_2_2.copy().set_color(WHITE).scale(0.8).next_to(tex_2,DOWN).align_to(tex_2,LEFT)
        self.wait()
        self.play(TransformFromCopy(sub_title_2[1],tex_3))
        self.wait()
        self.play(FadeOutAndShiftDown(sub_title_2))
        self.wait()
        sub_title_3_1 = Text("分别以",font='SetoFont SC')
        sub_title_3_2 = TexMobject("a_{k}").set_color(YELLOW).next_to(sub_title_3_1,RIGHT)
        sub_title_3_3 = Text("和", font='SetoFont SC').next_to(sub_title_3_2,RIGHT)
        sub_title_3_4 = TexMobject("b_{k}").set_color(YELLOW).next_to(sub_title_3_3, RIGHT)
        sub_title_3_5 = Text("为边长构造一堆矩形", font='SetoFont SC').next_to(sub_title_3_4, RIGHT)
        sub_title_3 = VGroup(sub_title_3_1,sub_title_3_2,sub_title_3_3,sub_title_3_4,sub_title_3_5).move_to(ORIGIN).shift(DOWN*3)
        tip = Text("(为了美观，矩形都用正方形表示)", font='SetoFont SC').set_color(YELLOW).scale(0.4).next_to(sub_title_3,DOWN*0.3).align_to(sub_title_3,RIGHT)
        self.play(FadeInFromPoint(sub_title_3,sub_title_3.get_center()))
        self.add(tip)
        self.wait()
        label_a_1 = TexMobject("a_{1}").scale(0.6).next_to(rec_group[0],UP*0.6)
        label_b_1 = TexMobject("b_{1}").scale(0.6).next_to(rec_group[0],RIGHT*0.6)
        self.play(FadeInFrom(rec_group[0],UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_1),FadeInFromLarge(label_b_1),run_time=0.5)
        label_a_2 = TexMobject("a_{2}").scale(0.6).next_to(rec_group[2],UP*0.6)
        label_b_2 = TexMobject("b_{2}").scale(0.6).next_to(rec_group[1],RIGHT*0.6)
        self.play(FadeInFrom(rec_group[1:3], UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_2), FadeInFromLarge(label_b_2),run_time=0.5)
        label_a_3 = TexMobject("...").rotate(PI/2).scale(0.6).next_to(rec_group[3], RIGHT * 0.6)
        label_b_3 = TexMobject("...").scale(0.6).next_to(rec_group[5], UP * 0.6)
        self.play(FadeInFrom(rec_group[3:6], UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_3), FadeInFromLarge(label_b_3),run_time=0.5)
        label_a_4 = TexMobject("a_{k}").scale(0.6).next_to(rec_group[9], UP * 0.6)
        label_b_4 = TexMobject("b_{k}").scale(0.6).next_to(rec_group[6], RIGHT * 0.6)
        self.play(FadeInFrom(rec_group[6:10], UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_4), FadeInFromLarge(label_b_4),run_time=0.5)
        label_a_5 = TexMobject("...").rotate(PI / 2).scale(0.6).next_to(rec_group[10], RIGHT * 0.6)
        label_b_5 = TexMobject("...").scale(0.6).next_to(rec_group[14], UP * 0.6)
        self.play(FadeInFrom(rec_group[10:15], UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_5), FadeInFromLarge(label_b_5),run_time=0.5)
        label_a_6 = TexMobject("a_{n}").scale(0.6).next_to(rec_group[20], UP * 0.6)
        label_b_6 = TexMobject("b_{n}").scale(0.6).next_to(rec_group[15], RIGHT * 0.6)
        self.play(FadeInFrom(rec_group[15:21], UP),run_time=0.5)
        self.play(FadeInFromLarge(label_a_6), FadeInFromLarge(label_b_6),run_time=0.5)
        self.wait(1.5)
        self.remove(tip)
        self.play(FadeOutAndShiftDown(sub_title_3))
        sub_title_4_1 = Text('"对角线"上矩形的面积之和记为', font='SetoFont SC')
        sub_title_4_2 = TexMobject("S_{1}").set_color(YELLOW).next_to(sub_title_4_1,RIGHT)
        sub_title_4 = VGroup(sub_title_4_1,sub_title_4_2)
        sub_title_4.move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeInFromPoint(sub_title_4,sub_title_4.get_center()))
        rec_opacity_group = VGroup(rec_group[1],rec_group[3:5],rec_group[6:9],rec_group[10:14],rec_group[15:20])
        self.play(ApplyMethod(rec_opacity_group.set_opacity,0.2))
        self.wait()
        tex_4 = TexMobject("S_{1}","=","a_{1}b_{1}","+","a_{2}b_{2}","+","...","=","\sum_{i=1}^{n} a_{i}b_{i}").scale(0.8).next_to(tex_3,DOWN).align_to(tex_3,LEFT)
        tex_4[0].set_color(YELLOW)
        self.play(TransformFromCopy(sub_title_4_2,tex_4[0]))
        self.play(Write(tex_4[1]))
        self.wait(0.5)
        label_a_1_rec = Rectangle().set_width(label_a_1.get_width()+0.2,stretch=True).set_height(label_a_1.get_height()+0.2,stretch=True).move_to(label_a_1.get_center()).set_fill(opacity=0).set_stroke(color=YELLOW,opacity=1)
        label_b_1_rec = label_a_1_rec.copy().move_to(label_b_1.get_center())
        self.play(FadeInFromLarge(label_a_1_rec),FadeInFromLarge(label_b_1_rec))
        self.wait(0.5)
        self.play(TransformFromCopy(rec_group[0],tex_4[2]))
        self.play(Write(tex_4[3]))
        label_a_2_rec = label_a_1_rec.copy().move_to(label_a_2.get_center())
        label_b_2_rec = label_a_1_rec.copy().move_to(label_b_2.get_center())
        self.play(Transform(label_a_1_rec,label_a_2_rec),Transform(label_b_1_rec,label_b_2_rec))
        self.wait(0.5)
        self.play(TransformFromCopy(rec_group[2],tex_4[4]))
        self.play(Write(tex_4[5]))
        self.wait(0.5)
        self.remove(label_a_1_rec,label_b_1_rec)
        self.play(ApplyMethod(label_a_2_rec.move_to,label_b_3.get_center()),ApplyMethod(label_b_2_rec.move_to, label_a_3.get_center()),run_time=0.5)
        self.play(ApplyMethod(label_a_2_rec.move_to, label_a_4.get_center()),
                  ApplyMethod(label_b_2_rec.move_to, label_b_4.get_center()), run_time=0.5)
        self.play(ApplyMethod(label_a_2_rec.move_to, label_b_5.get_center()),
                  ApplyMethod(label_b_2_rec.move_to, label_a_5.get_center()), run_time=0.5)
        self.play(ApplyMethod(label_a_2_rec.move_to, label_a_6.get_center()),
                  ApplyMethod(label_b_2_rec.move_to, label_b_6.get_center()), run_time=0.5)
        self.play(FadeInFromPoint(tex_4[6],tex_4[6].get_center()))
        self.play(FadeInFromLarge(tex_4[7:9]))
        self.wait()
        self.play(FadeOutAndShiftDown(tex_4[1:7]))
        self.play(ApplyMethod(tex_4[7:].next_to,tex_4[0],RIGHT))
        self.wait()
        sub_title_5_1 = Text('剩余部分的面积记为', font='SetoFont SC')
        sub_title_5_2 = TexMobject("S_{2}").set_color(YELLOW).next_to(sub_title_5_1, RIGHT)
        sub_title_5 = VGroup(sub_title_5_1, sub_title_5_2)
        sub_title_5.move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_4),FadeOut(label_a_2_rec),FadeOut(label_b_2_rec))
        self.play(ApplyMethod(rec_group.set_opacity,0.2),FadeInFromPoint(sub_title_5,sub_title_5.get_center()),ApplyMethod(rec_opacity_group.set_opacity,1))
        tex_5 = TexMobject("S_{2}","=","\sum_{i=2}^{n} A_{i-1}b_{i}","=\sum_{i=1}^{n-1}A_{i}b_{i+1}").scale(0.8).next_to(tex_4[8],RIGHT*1.2)
        tex_5[0].set_color(YELLOW)
        self.play(TransformFromCopy(sub_title_5_2,tex_5[0]))
        self.play(Write(tex_5[1]))
        self.wait(0.5)
        sub_title_6 = Text("总面积等于分面积之和", font='SetoFont SC').shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_5))
        self.play(FadeInFromPoint(sub_title_6,sub_title_6.get_center()))
        rec_2 =Polygon(rec_group[1].get_corner(UL),rec_group[1].get_corner(UR),rec_group[1].get_corner(DR),rec_group[1].get_corner(DL)).set_fill(RED,opacity=0.5).set_stroke(color=RED,opacity=1)
        rec_3 = Polygon(rec_group[4].get_corner(UL),rec_group[3].get_corner(UR),rec_group[3].get_corner(DR),rec_group[4].get_corner(DL)).set_fill(RED,opacity=0.5).set_stroke(color=RED,opacity=1)
        rec_k = Polygon(rec_group[8].get_corner(UL),rec_group[6].get_corner(UR),rec_group[6].get_corner(DR),rec_group[8].get_corner(DL)).set_fill(RED,opacity=0.5).set_stroke(color=RED,opacity=1)
        rec_5 = Polygon(rec_group[13].get_corner(UL),rec_group[10].get_corner(UR),rec_group[10].get_corner(DR),rec_group[13].get_corner(DL)).set_fill(RED,opacity=0.5).set_stroke(color=RED,opacity=1)
        rec_6 = Polygon(rec_group[19].get_corner(UL), rec_group[15].get_corner(UR), rec_group[15].get_corner(DR),
                        rec_group[19].get_corner(DL)).set_fill(RED, opacity=0.5).set_stroke(color=RED, opacity=1)
        self.play(ShowCreation(rec_2))
        self.play(ReplacementTransform(rec_2,rec_3),run_time=0.5)
        self.play(ReplacementTransform(rec_3, rec_k), run_time=0.5)
        self.play(ReplacementTransform(rec_k, rec_5), run_time=0.5)
        self.play(ReplacementTransform(rec_5, rec_6), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(rec_6, rec_3))
        self.wait(0.5)
        label_Ak = TexMobject("A_{k-1}").scale(0.8).set_color(YELLOW).next_to(rec_3,UP*0.3)
        label_bk = TexMobject("b_{k}").scale(0.8).set_color(YELLOW).next_to(rec_3, LEFT* 0.3)
        self.play(FadeInFromPoint(label_Ak,label_Ak.get_center()),FadeInFromPoint(label_bk,label_bk.get_center()))
        sub_title_7_1 = Text("第k层的面积可表示为", font='SetoFont SC')
        sub_title_7_2 = TexMobject("A_{k-1}b_{k}").set_color(YELLOW).next_to(sub_title_7_1,RIGHT)
        sub_title_7 = VGroup(sub_title_7_1,sub_title_7_2).move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_6))
        self.play(FadeInFromPoint(sub_title_7,sub_title_7.get_center()))
        self.wait(2)
        sub_title_8 = Text("将每一层的面积相加，得到总面积", font='SetoFont SC').shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_7))
        self.play(FadeInFromPoint(sub_title_8,sub_title_8.get_center()))
        self.wait()
        self.play(TransformFromCopy(rec_opacity_group,tex_5[2]))
        self.wait(0.5)
        self.play(FadeInFrom(tex_5[3],LEFT))
        self.wait(1.5)
        self.play(FadeOut(rec_3),FadeOut(label_Ak),FadeOut(label_bk),FadeOutAndShiftDown(sub_title_8),ApplyMethod(rec_group.set_opacity,1))
        sub_title_9_1 = Text("记全体矩形面积之和为", font='SetoFont SC')
        sub_title_9_2 = TexMobject("S").set_color(YELLOW).next_to(sub_title_9_1)
        sub_title_9 = VGroup(sub_title_9_1,sub_title_9_2).move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeInFromPoint(sub_title_9,sub_title_9.get_center()))
        sub_title_10 = TexMobject("S","=","\sum_{i=1}^{n} A_{i}b_{i}").shift(DOWN*2.5)
        sub_title_10[0].set_color(YELLOW)
        self.wait(2)
        self.play(FadeOutAndShiftDown(sub_title_9))
        self.play(FadeInFromPoint(sub_title_10,sub_title_10.get_center()))
        rec_1_1 = rec_group[0].copy().set_fill(YELLOW_A, opacity=0.5).set_stroke(color=YELLOW, opacity=1)
        rec_2_1 = rec_1_1.copy().set_width(1.6,about_point=rec_1_1.get_corner(DR),stretch=True).shift(DOWN*0.8).set_color(YELLOW_B)
        rec_3_1 = rec_1_1.copy().set_width(2.4, about_point=rec_1_1.get_corner(DR), stretch=True).shift(DOWN * 1.6).set_color(YELLOW_C)
        rec_4_1 = rec_1_1.copy().set_width(3.2, about_point=rec_1_1.get_corner(DR), stretch=True).shift(DOWN * 2.4).set_color(YELLOW_D)
        rec_5_1 = rec_1_1.copy().set_width(4, about_point=rec_1_1.get_corner(DR), stretch=True).shift(DOWN * 3.2).set_color(YELLOW_E)
        rec_6_1 = rec_1_1.copy().set_width(4.8, about_point=rec_1_1.get_corner(DR), stretch=True).shift(DOWN * 4).set_color(YELLOW)
        self.play(ShowCreation(rec_1_1))
        self.play(ReplacementTransform(rec_1_1,rec_2_1),run_time=0.5)
        self.play(ReplacementTransform(rec_2_1, rec_3_1), run_time=0.5)
        self.play(ReplacementTransform(rec_3_1, rec_4_1), run_time=0.5)
        self.play(ReplacementTransform(rec_4_1, rec_5_1), run_time=0.5)
        self.play(ReplacementTransform(rec_5_1, rec_6_1), run_time=0.5)
        self.wait()
        self.play(FadeOut(rec_6_1))
        tex_6 = TexMobject("S","=","\sum_{i=1}^{n} A_{i}b_{i}","=","\sum_{i=1}^{n-1} A_{i}b_{i}+A_{n}b_{n}").scale(0.8).next_to(tex_4,DOWN).align_to(tex_4,LEFT)
        tex_6[0].set_color(YELLOW)
        self.play(ReplacementTransform(sub_title_10,tex_6))
        self.wait()
        sub_title_11_1 = Text("又因为", font='SetoFont SC')
        sub_title_11_2 = TexMobject("S_{1}","=","S","-","S_{2}").next_to(sub_title_11_1,RIGHT)
        sub_title_11_2[0].set_color(YELLOW)
        sub_title_11_2[2].set_color(YELLOW)
        sub_title_11_2[4].set_color(YELLOW)
        sub_title_11 = VGroup(sub_title_11_1,sub_title_11_2).move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeInFromPoint(sub_title_11,sub_title_11.get_center()))
        self.wait()
        tex_7 = TexMobject("S_{1}","=","S","-","S_{2}").next_to(tex_3,DOWN*1.2).align_to(tex_3,LEFT)
        tex_7[0].set_color(YELLOW)
        tex_7[2].set_color(YELLOW)
        tex_7[4].set_color(YELLOW)
        tex_4_copy = VGroup(tex_4[:1].copy(),tex_4[-2:].copy()).scale(0.6).next_to(tex_1,RIGHT*7)
        tex_5_copy = tex_5.copy().scale(0.6).next_to(tex_4_copy,DOWN).align_to(tex_4_copy,LEFT)
        tex_6_copy = tex_6.copy().scale(0.6).next_to(tex_5_copy,DOWN).align_to(tex_4_copy,LEFT)
        tex_4_group = VGroup(tex_4[0],tex_4[-2:])
        self.play(ReplacementTransform(tex_4_group,tex_4_copy),ReplacementTransform(tex_5,tex_5_copy),ReplacementTransform(tex_6,tex_6_copy))
        #self.play(FadeOut(tex_4[:1]),FadeOut(tex_4[-2:]),FadeOut(tex_5),FadeOut(tex_6))
        self.play(TransformFromCopy(sub_title_11_2,tex_7))
        self.wait(1.5)
        sub_title_12_1 = Text("于是有", font='SetoFont SC').set_color(YELLOW).scale(0.8)
        sub_title_12_2 = TexMobject("\sum_{k=1}^{n}a_{k}b_{k} = \sum_{k=1}^{n-1}A_{k}(b_{k}-b_{k+1})+A_{n}b_{n}").scale(0.8).next_to(sub_title_12_1,RIGHT)
        sub_title_12 = VGroup(sub_title_12_1,sub_title_12_2).move_to(ORIGIN).shift(DOWN*2.5)
        self.play(FadeOutAndShiftDown(sub_title_11))
        self.play(FadeInFromPoint(sub_title_12,sub_title_12.get_center()))
        tex_8 = TexMobject("\sum_{i=1}^{n}a_{i}b_{i} = \sum_{i=1}^{n-1}A_{i}(b_{i}-b_{i+1})+A_{n}b_{n}").scale(0.8).next_to(tex_7,DOWN*2.3).align_to(tex_7,LEFT)
        rec_tex_8 = Rectangle().set_width(tex_8.get_width()+0.2,stretch=True).set_height(tex_8.get_height()+0.2,stretch=True).set_color(YELLOW).move_to(tex_8.get_center())
        self.wait()
        self.play(TransformFromCopy(sub_title_12_2,tex_8))
        self.play(ShowCreationThenDestructionAround(rec_tex_8,run_time=3))
        sub_title_13_1 = Text("这就是我们小学二年级就学过的", font='SetoFont SC')
        sub_title_13_2 = Text("阿贝尔变换", font='SetoFont SC').set_color(YELLOW).next_to(sub_title_13_1,RIGHT)
        sub_title_13 = VGroup(sub_title_13_1,sub_title_13_2).move_to(ORIGIN).shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_12))
        self.play(FadeInFromPoint(sub_title_13,sub_title_13.get_center()))
        self.wait(2)
        sub_title_14 = Text("可简记为", font='SetoFont SC').shift(DOWN*3)
        sub_title_15 = Text("对角线面积=大阶梯面积-小阶梯面积", font='SetoFont SC').shift(DOWN*3)
        self.play(FadeOutAndShiftDown(sub_title_13))
        self.play(FadeInFromPoint(sub_title_14,sub_title_14.get_center()))
        self.wait()
        self.play(FadeOutAndShiftDown(sub_title_14))
        self.play(FadeInFromPoint(sub_title_15, sub_title_15.get_center()))
        self.wait(5)