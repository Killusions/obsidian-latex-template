import pandas as pd

from wandb_downloader import WandbDownloader


# Replace `example_config_param` with the actual parameter name(s) you want to use



def GET_RUN_CONFIGURATIONS(name, example_config_param=None):
    return [
        {"project": f"dspro-predicting-{name}", "example_config_param": example_config_param}
    ]


class BestRunLoader:
    def __init__(self, entity, metric_name, project_names, file_names_to_download):
        self.entity = entity
        self.metric_name = metric_name
        self.project_names = project_names
        self.file_names_to_download = file_names_to_download
        self.configurations = self.create_configurations()
        self.results = self.load_results()

    def create_configurations(self):
        configurations = {}
        for name in self.project_names:
            example_config_param = None
            configurations[name] = GET_RUN_CONFIGURATIONS(name, example_config_param=example_config_param)
        return configurations

    def load_best_runs(self, project, data_augmentation, datasize, image_size):
        metric_ascending = False
        # Set metric_ascending to True if the metric is a loss/distance metric
        downloader = WandbDownloader(self.entity, project, data_augmentation, datasize, image_size)
        return downloader.get_and_collect_best_runs(self.metric_name, self.file_names_to_download, metric_ascending=metric_ascending)

    def load_results(self):
        results = {}
        for configs in self.configurations.values():
            for config in configs:
                key = f"{config['project']}_{config['example_config_param']}"
                results[key] = self.load_best_runs(config["project"], config["example_config_param"])
        return results

    def get_summary_table(self):
        summary = []
        for key, value in self.results.items():
            project, example_config_param = key.split("_")
            summary.append({"Project": project, "Example config param": example_config_param, "Number of Runs": len(value)})
        df = pd.DataFrame(summary)
        return df

    def display_summary_table(self):
        df = self.get_summary_table()
        print(df)

    def count_runs_per_project(self):
        project_counts = {}
        for key in self.results:
            project = key.split("_")[0]
            if project not in project_counts:
                project_counts[project] = 0
            project_counts[project] += len(self.results[key])
        return project_counts
