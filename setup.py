import setuptools

if __name__ == "__main__":
    setuptools.setup(
        entry_points={'console_scripts': ['phyDataPopulation=Physical_data_population.read_CLI_n_run:main_method',
                                          'phyDataPopulation_tmp=Physical_data_population.read_CLI_n_run_temp:main_method']},
        install_requires=['pyxlsb==1.0.5', 'xlrd'],
        extras_require={'test': ['pytest>=3.7'], 'dev':[]}
    )
