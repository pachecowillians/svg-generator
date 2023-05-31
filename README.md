![A.svg](./avatar/img/A.svg) &nbsp;
![B.svg](./avatar/img/B.svg) &nbsp;
![C.svg](./avatar/img/C.svg) &nbsp;
![D.svg](./avatar/img/D.svg) &nbsp;
![E.svg](./avatar/img/E.svg) &nbsp;
![F.svg](./avatar/img/F.svg) &nbsp;
![G.svg](./avatar/img/G.svg) &nbsp;
![H.svg](./avatar/img/H.svg) &nbsp;
![I.svg](./avatar/img/I.svg) &nbsp;
![J.svg](./avatar/img/J.svg) &nbsp;
![K.svg](./avatar/img/K.svg) &nbsp;
![L.svg](./avatar/img/L.svg) &nbsp;
![M.svg](./avatar/img/M.svg) &nbsp;
![N.svg](./avatar/img/N.svg) &nbsp;
![O.svg](./avatar/img/O.svg) &nbsp;
![P.svg](./avatar/img/P.svg) &nbsp;
![Q.svg](./avatar/img/Q.svg) &nbsp;
![R.svg](./avatar/img/R.svg) &nbsp;
![S.svg](./avatar/img/S.svg) &nbsp;
![T.svg](./avatar/img/T.svg) &nbsp;
![U.svg](./avatar/img/U.svg) &nbsp;
![V.svg](./avatar/img/V.svg) &nbsp;
![W.svg](./avatar/img/W.svg) &nbsp;
![X.svg](./avatar/img/X.svg) &nbsp;
![Y.svg](./avatar/img/Y.svg) &nbsp;
![Z.svg](./avatar/img/Z.svg) &nbsp;

<br/>

![250x250.svg](./banner/img/250x250.svg)
![250x250.svg](./banner/img/120x240.svg)
![250x250.svg](./banner/img/468x60.svg)


# SVG Generator

<p align="center">
  <a href="https://www.docker.com/"><img src="https://raw.githubusercontent.com/pachecowillians/svg-icons/0ca246100b279696cc5b393452ad2aa8758de59a/img/svg.svg" alt="Docker" height="100px"></a>
</p>

This project is a collection of tools that generate SVG images for specific purposes. Currently, the available tools are an avatar generator and a banner generator.

All the generated images have a random background color and are built using the Pycairo library.

To install the Pycairo library, run the following command:

```sh
pip install pycairo
```

Once Pycairo is installed, you can run the individual projects to generate avatars and banners. The generated images will be saved in the respective `img` folders of each project.

## Running the Projects

Start by cloning the repository using `git clone`:

```sh
git clone https://github.com/pachecowillians/svg-generator.git
```

After cloning the repository, navigate to the project folder using `cd`:

```sh
cd svg-generator
```

### Generating Avatars

To generate avatars, run the Python file located in the `avatar/` folder:

```sh
python3 avatar/avatar.py
```

Running the above command will generate avatars and save them in the `avatar/img/` folder.

### Generating Banners

To generate banners, run the Python file located in the `banner/` folder:

```sh
python3 banner/banner.py
```

Running the above command will generate banners and save them in the `banner/img/` folder.