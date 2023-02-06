Print time (inference-only)
        LOGGER.info(f'{s}Done. ({t3 - t2:.3f}s)')


        if "1 100" in s:
            print(cc)
            if(cc < 3):
                print("updating cc")
                a = "Its 100 rupee"
                os.system('espeak "{}"'.format(a))


        elif "done" in s:
            do = "waiting"
            os.system('espeak "{}"'.format(do))

        elif "1 500" in s:
            b = "Its 500 rupee"
            os.system('espeak "{}"'.format(b))

        elif "1 2000" in s:
            c = "Its 2000 rupee"
            os.system('espeak "{}"'.format(c))

        elif "1 10" in s:
            d = "Its 10 rupee"
            os.system('espeak "{}"'.format(d))

        elif "1 200" in s:
            print(cc)
            if (cc < 3):
                print("updating cc")
                a = "Its 200 rupee"
                os.system('espeak "{}"'.format(a))

        elif "1 20" in s:
            e = "Its 20 rupee"
            os.system('espeak "{}"'.format(e))

        elif "1 50" in s:
            f = "Its 50 rupee"
            os.system('espeak "{}"'.format(f))

        else:
            cc=0
            g = "NO  rupee detected"
            os.system('espeak "{}"'.format(g))


    # Print results
    t = tuple(x / seen * 1E3 for x in dt)  # speeds per image
    LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
