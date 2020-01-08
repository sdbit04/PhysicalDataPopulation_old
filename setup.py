import setuptools

if __name__ == "__main__":
    setuptools.setup(
        entry_points={'console_scripts': ['phyDataPopulation = Physical_data_population.read_CLI_n_run:main_method']}, install_requires=['pyxlsb', 'xlrd']



    )
