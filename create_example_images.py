from __future__ import print_function, division
from laplotter import LossAccPlotter
from check_laplotter import show_chart, add_noise
import numpy as np

def main():
    nb_points = 500

    loss_train = add_noise(np.linspace(0.9, 0.1, num=nb_points), 0.025)
    loss_val = add_noise(np.linspace(0.7, 0.3, num=nb_points), 0.045)
    acc_train = add_noise(np.linspace(0.52, 0.95, num=nb_points), 0.025)
    acc_val = add_noise(np.linspace(0.65, 0.75, num=nb_points), 0.045)

    # Normal example plot
    lap = LossAccPlotter(save_to_filepath="example_plot.jpg")
    show_chart(loss_train, loss_val, acc_train, acc_val, lap=lap,
               title="Example Plot with Loss and Accuracy")

    # Plot showing only the results of the loss function (accuracy off)
    lap = LossAccPlotter(show_acc_plot=False,
                         save_to_filepath="example_plot_loss.jpg")
    show_chart(loss_train, loss_val, acc_train, acc_val, lap=lap,
               title="Example Plot, only Loss Function")

    # Plot showing only training dataset values (but for both loss and accuracy)
    lap = LossAccPlotter(save_to_filepath="example_plot_only_training.jpg")
    show_chart(loss_train, np.array([]), acc_train, np.array([]), lap=lap,
               title="Example Plot, only Training Dataset / no Validation Dataset")

    # Plot with a different update interval for training and validation dataset
    # (i.e. only one validation value for every 10 training values)
    #
    # Set 9 out of 10 validation values to -1, which will be transformed into
    # None in show_chart(). (same technique as in check_laplotter.py)
    nb_points_train = nb_points
    nb_points_val = int(nb_points * 0.1)
    all_indices = np.arange(0, nb_points_train-1, 1)
    keep_indices = np.arange(0, nb_points_train-1, int(nb_points_train / nb_points_val))
    set_to_none_indices = np.delete(all_indices, keep_indices)
    loss_val[set_to_none_indices] = -1.0
    acc_val[set_to_none_indices] = -1.0
    lap = LossAccPlotter(show_acc_plot=False,
                         save_to_filepath="example_plot_update_intervals.jpg")
    show_chart(loss_train, loss_val, acc_train, acc_val, lap=lap,
               title="Example Plot with different Update Intervals for Training " \
                     "and Validation Datasets")

if __name__ == "__main__":
    main()
